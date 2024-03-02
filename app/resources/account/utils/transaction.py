"""
file_name = transaction.py
Created On: 2024/03/01
Lasted Updated: 2024/03/01
Description: _FILL OUT HERE_
Edit Log:
2024/03/01
    - Created file
"""

# STANDARD LIBRARY IMPORTS
from datetime import datetime
from enum import Enum
from operator import add, sub
from typing import Callable, Dict, Final, TypedDict

# THIRD PARTY LIBRARY IMPORTS

# LOCAL LIBRARY IMPORTS


class TransactionType(Enum):
    """_summary_

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

    # POSITIVE OPERATORS
    DEPOSIT = "DEPOSIT"
    POSITIVE_INTEREST = "INTEREST"
    DIVIDEND = "DIVIDEND"
    # NEGATIVE OPERATORS
    WITHDRAWAL = "WITHDRAWAL"
    PAYMENT = "PAYMENT"
    NEGATIVE_INTEREST = "NEGATIVE_INTEREST"


class Transaction(TypedDict):
    """
    _summary_

    Args:
        TypedDict (_type_): _description_
    """

    transaction_type: TransactionType
    transaction_description: str
    transaction_date: datetime
    transaction_amount: float


TRANSACTION_OPERATORS: Final[Dict[TransactionType, Callable[[float, float], float]]] = {
    # POSITIVE OPERATORS
    TransactionType.DEPOSIT: add,
    TransactionType.POSITIVE_INTEREST: add,
    TransactionType.DIVIDEND: add,
    # NEGATIVE OPERATORS
    TransactionType.WITHDRAWAL: sub,
    TransactionType.PAYMENT: sub,
    TransactionType.NEGATIVE_INTEREST: sub,
}
