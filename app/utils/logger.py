"""
file_name = logger.py
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
from typing import Generator

import logging.config

from logging import Logger, Formatter
from logging.handlers import TimedRotatingFileHandler

# LOCAL LIBRARY IMPORTS


class AppLogger:
    """
    A class used to create a logger for the application
    """

    @staticmethod
    def add_handler() -> None:
        handler: TimedRotatingFileHandler = logging.handlers.TimedRotatingFileHandler(
            f"{environ['LOGGING_FOLDER_PATH']}/app.log", when="midnight"
        )

        handler.suffix = "%Y%m%d"
        formatter: Formatter = Formatter(
            fmt="%(asctime)s | %(pathname)s | \
            %(levelname)-8s | %(filename)s-%(funcName)s-%(lineno)04d | \
            %(message)s"
        )
        handler.setFormatter(formatter)
        logging.getLogger().addHandler(handler)

    @staticmethod
    def logging_setup() -> None:
        logging.config.fileConfig(environ["LOGGING_CONFIG_PATH"])
        AppLogger.add_handler()

    @staticmethod
    def get_logger() -> Generator[Logger, Logger, Logger]:
        assert AppLogger.logging_setup()

        while True:
            yield logging.getLogger()
