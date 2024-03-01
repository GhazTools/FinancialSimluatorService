"""
file_name = conftest.py
Created On: 2024/02/29
Lasted Updated: 2024/02/29
Description: _FILL OUT HERE_
Edit Log:
2024/02/29
    - Created file
"""

# STANDARD LIBRARY IMPORTS
from os import environ

# THIRD PARTY LIBRARY IMPORTS
from dotenv import load_dotenv
from pytest import fixture

from token_granter_wrapper.token_granter import (
    set_token_granter_url,
    grant_access_token,
)

# LOCAL LIBRARY IMPORTS


# PYTEST CONFIGURATION
def pytest_configure():
    load_dotenv()
    set_token_granter_url(environ["TOKEN_GRANTER_URL"])


def pytest_addoption(parser):
    parser.addoption("--username", action="store", default="")
    parser.addoption("--password", action="store", default="")


# GLOBAL FIXTURES
@fixture(name="token_username")
def fixture_username(request) -> str:
    return str(request.config.getoption("--username"))


@fixture(name="token_password")
def fixture_token(request, token_username: str) -> str:
    password = request.config.getoption("--password")
    return str(grant_access_token(token_username, password, True))
