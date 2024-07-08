from typing import NamedTuple
from datetime import date

class Reserve(NamedTuple):
    id: str
    reserve_date: date
    payment: float
    balance_due: float
