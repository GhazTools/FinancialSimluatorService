"""
file_name = resource_map.py
Created On: 2024/02/28
Lasted Updated: 2024/02/28
Description: _FILL OUT HERE_
Edit Log:
2024/02/28
    - Created file
"""

# STANDARD LIBRARY IMPORTS
from typing import Any, TypedDict

# THIRD PARTY LIBRARY IMPORTS

# LOCAL LIBRARY IMPORTS


class ResourceMap(TypedDict):
    """
    A class used within every resource.py class to make it easier to map objects
    """

    resourceClass: Any
    endpoint: str
    include: bool
