"""
file_name = resource,.py
Created On: 2024/02/28
Lasted Updated: 2024/02/28
Description: _FILL OUT HERE_
Edit Log:
2024/02/28
    - Created file
"""

# STANDARD LIBRARY IMPORTS
from typing import List

# THIRD PARTY LIBRARY IMPORTS

# LOCAL LIBRARY IMPORTS
from app.resources.resource_map import ResourceMap


# pylint: disable=too-few-public-methods
class AddAccountResource:
    """
    _summary_
    """

    async def on_post(self, req, resp) -> None:
        """_summary_

        Args:
            req (_type_): _description_
            resp (_type_): _description_
        """
        print(req, resp)


RESOURCES: List[ResourceMap] = [
    {"resourceClass": AddAccountResource, "endpoint": "/addAccount", "include": True}
]
