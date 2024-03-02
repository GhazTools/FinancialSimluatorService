"""
file_name = account.py
Created On: 2024/03/01
Lasted Updated: 2024/03/01
Description: _FILL OUT HERE_
Edit Log:
2024/03/01
    - Created file
"""

# STANDARD LIBRARY IMPORTS
from copy import copy

from typing import Dict

# THIRD PARTY LIBRARY IMPORTS

# LOCAL LIBRARY IMPORTS
from app.resources.account.utils.statement import Statement


class Account:
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
        account_name: str,
        description: str,
        current_balance: float,
        monthly_contribution: float,
    ) -> None:
        self.__account_name = account_name
        self.__description = description
        self.__current_balance = current_balance
        self.__monthly_contribution = monthly_contribution
        self.__account_statements: Dict[str, Statement] = {}

    # PROPERTIES START HERE
    @property
    def account_name(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return self.__account_name

    @account_name.setter
    def account_name(self, account_name: str) -> None:
        """_summary_

        Args:
            account_name (str): _description_
        """
        self.__account_name = account_name

    @property
    def description(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return self.__description

    @description.setter
    def description(self, description: str) -> None:
        """_summary_

        Args:
            description (str): _description_
        """
        self.__description = description

    @property
    def current_balance(self) -> float:
        """_summary_

        Returns:
            float: _description_
        """
        return self.__current_balance

    @current_balance.setter
    def current_balance(self, current_balance: float) -> None:
        """_summary_

        Args:
            current_balance (float): _description_
        """
        self.__current_balance = current_balance

    @property
    def monthly_contribution(self) -> float:
        """_summary_

        Returns:
            float: _description_
        """
        return self.__monthly_contribution

    @monthly_contribution.setter
    def monthly_contribution(self, monthly_contribution: float) -> None:
        """_summary_

        Args:
            monthly_contribution (float): _description_
        """
        self.__monthly_contribution = monthly_contribution

    @property
    def account_statements(self) -> dict:
        """_summary_

        Returns:
            dict: _description_
        """
        return copy(self.__account_statements)

    # PROPERTIES END HERE

    # PUBLIC METHODS START HERE
    def withdraw(self, amount: float) -> bool:
        """_summary_

        Args:
            amount (float): _description_

        Returns:
            bool: _description_
        """
        if amount > self.__current_balance:
            return False

        self.__current_balance -= amount
        return True

    def deposit(self, amount: float) -> None:
        """_summary_

        Args:
            amount (float): _description_
        """
        self.__current_balance += amount

    # PUBLIC METHODS END HERE

    # PRIVATE METHODS START HERE
    # def __add_to_statement()
    # PRIVATE METHODS END HERE
