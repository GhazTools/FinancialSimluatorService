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

from ghaz_function_timer.timer import Timer

# LOCAL LIBRARY IMPORTS
from app.resources.resource_endpoint import ResourceEndpoint
from app.utils.logger import AppLogger
from app.utils.module_loader import ModuleLoader

# GLOBALS START HERE
IGNORE_FOLDERS: Set[str] = {"__pycache__", "shared_resource_utils"}
RESOURCE_FILE_NAME: str = "resource.py"


def get_feature_endpoints(
    full_feature_path: str, main_feature: str
) -> List[ResourceEndpoint]:
    """
    This function will get all the resources from a feature directory and return it as a list
    """

    resources: List[ResourceEndpoint] = []

    for feature_object in listdir(full_feature_path):
        endpoint_branch = f"/{main_feature}/{feature_object}"
        full_path: str = join(full_feature_path, feature_object)

        if not (
            isdir(full_path)
            and not feature_object in IGNORE_FOLDERS
            and RESOURCE_FILE_NAME in listdir(full_path)
        ):
            continue

        resource_path: str = join(full_path, RESOURCE_FILE_NAME)

        module_resources: ResourceEndpoint = cast(
            ResourceEndpoint,
            ModuleLoader.load_object_from_module(
                resource_path, f"resource_{len(resources)}", "RESOURCE"
            ),
        )

        if not module_resources["include"]:
            continue

        module_resources["endpoint"] = (
            endpoint_branch
            if not module_resources["endpoint"]
            else module_resources["endpoint"]
        )
        resources.append(module_resources)

    return resources


def get_all_resources() -> List[ResourceEndpoint]:
    """
    This function will get all the resources from the resources directory and return it as a list
    """

    resource_directory: str = realpath((dirname((__file__))))
    resources: List[ResourceEndpoint] = []

    for directory_object in listdir(resource_directory):
        feature_path: str = join(resource_directory, directory_object)

        if not isdir(feature_path):
            continue

        resources.extend(get_feature_endpoints(feature_path, directory_object))

    return resources


@Timer(print_time=True, print_response=False, log_not_print=True)
def register_routes(app: App) -> None:
    """
    This function will register all the resources in the resources directory
    """

    resources: List[ResourceEndpoint] = get_all_resources()

    for resource in resources:
        endpoint: str = cast(str, resource["endpoint"])
        app.add_route(endpoint, resource["resourceClass"]())
        AppLogger.log(f"Registered route: {endpoint}")
