from typing import NamedTuple
from datetime import datetime

from .user import User
from .product import Product


class Reserve(NamedTuple):
    id: str
    product: Product
    user: User
    reserve_date: datetime
    payment: float
    balance_due: float
