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


# THIRD PARTY LIBRARY IMPORTS

# LOCAL LIBRARY IMPORTS
from app.resources.resource_endpoint import (
    ResourceEndpoint,
    create_resource_endpoint_object,
)


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


RESOURCE: ResourceEndpoint = create_resource_endpoint_object(
    AddAccountResource, None, True
)
