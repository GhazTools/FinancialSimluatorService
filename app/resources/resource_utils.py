"""
file_name = resource_utils.py
Created On: 2024/02/29
Lasted Updated: 2024/02/29
Description: _FILL OUT HERE_
Edit Log:
2024/02/29
    - Created file
"""

# STANDARD LIBRARY IMPORTS
from os import listdir
from os.path import dirname, isdir, join, realpath

from typing import List, Set, cast

# THIRD PARTY LIBRARY IMPORTS
from falcon.asgi import App

# LOCAL LIBRARY IMPORTS
from app.resources.resource_map import ResourceMap
from app.utils.logger import AppLogger
from app.utils.module_loader import ModuleLoader

# GLOBALS START HERE
IGNORE_FOLDERS: Set[str] = {"__pycache__"}
RESOURCE_FILE_NAME: str = "resource.py"


def extract_applicable_resources(resources: List[ResourceMap]) -> List[ResourceMap]:
    """
    Extracts a list of applicable resources that can be added to the app
    """

    valid_resources: List[ResourceMap] = []

    for resource in resources:
        if not resource["include"]:
            continue

        valid_resources.append(resource)

    return valid_resources


def get_all_resources() -> List[ResourceMap]:
    """
    This function will get all the resources from the resources directory and return it as a list
    """

    resource_directory: str = realpath((dirname((__file__))))
    resources: List[ResourceMap] = []

    for directory_object in listdir(resource_directory):
        feature_path: str = join(resource_directory, directory_object)

        if not isdir(feature_path):
            continue

        for feature_object in listdir(feature_path):
            full_path: str = join(feature_path, feature_object)

            if (
                isdir(full_path)
                and not directory_object in IGNORE_FOLDERS
                and RESOURCE_FILE_NAME in listdir(full_path)
            ):
                resource_path: str = join(full_path, RESOURCE_FILE_NAME)

                module_resources: List[ResourceMap] = cast(
                    List[ResourceMap],
                    ModuleLoader.load_object_from_module(
                        resource_path, f"resource_{len(resources)}", "RESOURCES"
                    ),
                )

                resources.extend(extract_applicable_resources(module_resources))

    return resources


def register_routes(app: App) -> None:
    """
    This function will register all the resources in the resources directory
    """

    resources: List[ResourceMap] = get_all_resources()

    for resource in resources:
        endpoint: str = resource["endpoint"]
        app.add_route(endpoint, resource["resourceClass"]())
        AppLogger.log(f"Registered route: {endpoint}")
