"""
file_name = resource_endpoint.py
Created On: 2024/02/28
Lasted Updated: 2024/02/28
Description: _FILL OUT HERE_
Edit Log:
2024/02/28
    - Created file
"""

# STANDARD LIBRARY IMPORTS
from typing import Any, TypedDict, Optional

# THIRD PARTY LIBRARY IMPORTS

# LOCAL LIBRARY IMPORTS


class ResourceEndpoint(TypedDict):
    """
    A class used within every resource.py class to make it easier to map objects
    """

    resourceClass: Any
    endpoint: Optional[str]
    include: bool


def create_resource_endpoint_object(
    resource_class: Any, endpoint: Optional[str], include: bool
) -> ResourceEndpoint:
    return {
        "resourceClass": resource_class,
        "endpoint": endpoint,
        "include": include,
    }
