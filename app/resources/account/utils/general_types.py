"""
file_name = general_types.py
Created On: 2024/03/01
Lasted Updated: 2024/03/01
Description: _FILL OUT HERE_
Edit Log:
2024/03/01
    - Created file
"""

# STANDARD LIBRARY IMPORTS
from datetime import datetime
from typing import Optional, TypedDict

# THIRD PARTY LIBRARY IMPORTS

# LOCAL LIBRARY IMPORTS


class DateRange(TypedDict):
    """_summary_

    Args:
        TypedDict (_type_): _description_
    """

    start_date: datetime
    end_date: Optional[datetime]
