"""
file_name = app.py
Created On: 2024/02/25
Lasted Updated: 2024/02/25
Description: _FILL OUT HERE_
Edit Log:
2024/02/25
    - Created file
"""

# STANDARD LIBRARY IMPORTS
from typing import Final

# THIRD PARTY LIBRARY IMPORTS
from falcon.asgi import App


# LOCAL LIBRARY IMPORTS
from app.resources.resource_utils import register_routes
from app.utils.logger import AppLogger


AppLogger.log("Instantiating app")

APP: Final[App] = App()
register_routes(APP)

AppLogger.log("Finished instantiating app")
