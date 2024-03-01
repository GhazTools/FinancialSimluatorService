"""
file_name = app_starter.py
Created On: 2024/03/01
Lasted Updated: 2024/03/01
Description: _FILL OUT HERE_
Edit Log:
2024/03/01
    - Created file
"""

# STANDARD LIBRARY IMPORTS

# THIRD PARTY LIBRARY IMPORTS
from falcon.asgi import App

from ghaz_function_timer.timer import Timer

# LOCAL LIBRARY IMPORTS
from app.resources.resource_utils import register_routes
from app.utils.logger import AppLogger
from app.utils.middleware import Middleware


@Timer(print_time=True, print_response=False)
def create_app() -> App:
    AppLogger.log("Instantiating app.")

    app: App = App(middleware=[Middleware()])
    register_routes(app)

    AppLogger.log("Finished instantiating app.")
