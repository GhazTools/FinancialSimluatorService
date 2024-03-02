"""
file_name = statement.py
Created On: 2024/03/01
Lasted Updated: 2024/03/01
Description: _FILL OUT HERE_
Edit Log:
2024/03/01
    - Created file
"""

# STANDARD LIBRARY IMPORTS
from datetime import datetime
from typing import Callable

# THIRD PARTY LIBRARY IMPORTS

# LOCAL LIBRARY IMPORTS
from app.resources.account.utils.transaction import (
    Transaction,
    TransactionType,
    TRANSACTION_OPERATORS,
)


class Statement:
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
        statement_start_date: datetime,
        statement_end_date: datetime,
        starting_balance: float,
    ) -> None:
        self.__statement_start_date = statement_start_date
        self.__statement_end_date = statement_end_date
        self.__starting_balance = starting_balance
        self.__ending_balance = starting_balance
        self.__transactions: list[Transaction] = []

    # PROPERTIES START HERE
    @property
    def statement_start_date(self) -> datetime:
        """_summary_

        Returns:
            datetime: _description_
        """

        return self.__statement_start_date

    @property
    def statement_end_date(self) -> datetime:
        """_summary_

        Returns:
            datetime: _description_
        """
        return self.__statement_end_date

    @property
    def starting_balance(self) -> float:
        """_summary_

        Returns:
            float: _description_
        """
        return self.__starting_balance

    @property
    def ending_balance(self) -> float:
        """_summary_

        Returns:
            float: _description_
        """
        return self.__ending_balance

    @property
    def transactions(self) -> list[Transaction]:
        """_summary_

        Returns:
            list[Transaction]: _description_
        """
        return self.__transactions

    # PROPERTIES END HERE

    # PUBLIC METHODS START HERE
    def add_transaction(self, transaction: Transaction) -> None:
        """_summary_

        Args:
            transaction_type (TransactionType): _description_
            transaction_description (str): _description_
            transaction_date (datetime): _description_
            transaction_amount (float): _description_
        """
        self.__transactions.append(transaction)
        self.__update_balance_from_transaction(transaction)

    # PUBLIC METHODS END HERE

    # PRIVATE METHODS START HERE
    def __update_balance_from_transaction(self, transaction: Transaction) -> None:
        """_summary_

        Args:
            transaction (Transaction): _description_
        """
        transaction_type: TransactionType = transaction["transaction_type"]
        transaction_operator: Callable[[float, float], float] = TRANSACTION_OPERATORS[
            transaction_type
        ]

        self.__ending_balance = transaction_operator(
            self.__ending_balance, transaction["transaction_amount"]
        )

    # PRIVATE METHODS END HERE
