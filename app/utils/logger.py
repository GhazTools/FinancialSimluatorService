"""
file_name = logger.py
Created On: 2024/02/29
Lasted Updated: 2024/02/29
Description: _FILL OUT HERE_
Edit Log:
2024/02/29
    - Created file
"""

# THIRD PARTY LIBRARY IMPORTS
import logging.config

from typing import cast

# STANDARD LIBRARY IMPORTS
from enum import Enum
from logging import CRITICAL, DEBUG, ERROR, INFO, NOTSET, WARNING, Formatter, Logger
from logging.handlers import TimedRotatingFileHandler
from os import environ

# LOCAL LIBRARY IMPORTS


class LoggingLevel(Enum):
    """
    A class used to create a logging level
    """

    NOT_SET = NOTSET
    DEBUG = DEBUG
    INFO = INFO
    WARNING = WARNING
    ERROR = ERROR
    CRITICAL = CRITICAL


class AppLogger:
    """
    A class used to create a logger for the application
    """

    __is_logging_setup: bool = False
    __logger: Logger | None = None

    @staticmethod
    def add_handler(logger: Logger) -> None:
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
        logger.addHandler(handler)

    @staticmethod
    def logging_setup(logging_level=LoggingLevel.INFO) -> None:
        if AppLogger.__is_logging_setup:
            return

        logging.config.fileConfig(environ["LOGGING_CONFIG_PATH"])
        logger: Logger = logging.getLogger()

        AppLogger.__logger = logger
        AppLogger.add_handler(logger)
        logger.setLevel(level=logging_level.value)

        AppLogger.__is_logging_setup = True

    @staticmethod
    def get_logger() -> Logger:
        AppLogger.logging_setup()
        return cast(Logger, AppLogger.__logger)

    @staticmethod
    def log(log_string: str, log_level: LoggingLevel = LoggingLevel.INFO) -> None:
        AppLogger.get_logger().log(level=log_level.value, msg=log_string)
