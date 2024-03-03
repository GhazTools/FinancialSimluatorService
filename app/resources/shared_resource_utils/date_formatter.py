"""
file_name = date_formatter.py
Created On: 2024/03/02
Lasted Updated: 2024/03/02
Description: _FILL OUT HERE_
Edit Log:
2024/03/02
    - Created file
"""

# STANDARD LIBRARY IMPORTS
from datetime import datetime
from enum import Enum

# THIRD PARTY LIBRARY IMPORTS

# LOCAL LIBRARY IMPORTS


class CommonDateFormats(Enum):
    """_summary_

    Args:
        Enum (_type_): _description_
    """

    MONTH_DAY_COMMA_YEAR = "%B %d, %Y"
    MONTH_DAY_COMMA_YEAR_HOUR_MINUTE = "%B %d, %Y %H:%M"


def format_date(date: datetime, date_format: CommonDateFormats) -> str:
    return date.strftime(date_format.value)
