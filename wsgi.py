"""
file_name = wsgi.py
Created On: 2024/02/29
Lasted Updated: 2024/02/29
Description: _FILL OUT HERE_
Edit Log:
2024/02/29
    - Created file
"""

# STANDARD LIBRARY IMPORTS

# THIRD PARTY LIBRARY IMPORTS
from uvicorn import run

# LOCAL LIBRARY IMPORTS
from app.app import APP

application = APP  # pylint: disable=invalid-name

if __name__ == "__main__":
    run(application, host="0.0.0.0", port=8000, lifespan="off")
