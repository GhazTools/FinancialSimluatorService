"""
file_name = income_source.py
Created On: 2024/03/01
Lasted Updated: 2024/03/01
Description: _FILL OUT HERE_
Edit Log:
2024/03/01
    - Created file
"""

# STANDARD LIBRARY IMPORTS
from datetime import datetime

# THIRD PARTY LIBRARY IMPORTS

# LOCAL LIBRARY IMPORTS
from app.resources.account.utils.general_types import DateRange


class IncomeSource:
    """
    __FILL OUT HERE_

    Args:
        arg1 (type): description
        ...

    Attributes:
        attr1 (type): description
        ...

    Properties:
        prop1 (type): description
        ...

    Methods:
        methodName: description
        ...

    """

    def __init__(
        self,
        source_name: str,
        date_range: DateRange,
        annual_salary: float,
        annual_bonus: float,
    ) -> None:
        self.__source_name = source_name
        self.__start_date = date_range["start_date"]
        self.__end_date = date_range["end_date"]
        self.__annual_salary = annual_salary
        self.__annual_bonus = annual_bonus

    # PROPERTIES START HERE
    @property
    def source_name(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return self.__source_name

    @source_name.setter
    def source_name(self, source_name: str) -> None:
        """_summary_

        Args:
            source_name (str): _description_
        """
        self.__source_name = source_name

    @property
    def start_date(self) -> datetime:
        """_summary_

        Returns:
            datetime: _description_
        """
        return self.__start_date

    @start_date.setter
    def start_date(self, start_date: datetime) -> None:
        """_summary_

        Args:
            start_date (datetime): _description_
        """
        self.__start_date = start_date

    @property
    def end_date(self) -> datetime | None:
        """_summary_

        Returns:
            datetime | None: _description_
        """
        return self.__end_date

    @end_date.setter
    def end_date(self, end_date: datetime | None) -> None:
        """_summary_

        Args:
            end_date (datetime | None): _description_
        """
        self.__end_date = end_date

    @property
    def annual_salary(self) -> float:
        """_summary_

        Returns:
            float: _description_
        """
        return self.__annual_salary

    @annual_salary.setter
    def annual_salary(self, annual_salary: float) -> None:
        """_summary_

        Args:
            annual_salary (float): _description_
        """
        self.__annual_salary = annual_salary

    @property
    def annual_bonus(self) -> float:
        """_summary_

        Returns:
            float: _description_
        """
        return self.__annual_bonus

    @annual_bonus.setter
    def annual_bonus(self, annual_bonus: float) -> None:
        """_summary_

        Args:
            annual_bonus (float): _description_
        """
        self.__annual_bonus = annual_bonus

    # PROPERTIES END HERE

    # PUBLIC METHODS START HERE
    # PUBLIC METHODS END HERE

    # PRIVATE METHODS START HERE
    # PRIVATE METHODS END HERE
