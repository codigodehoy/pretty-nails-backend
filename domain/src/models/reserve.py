from typing import NamedTuple
from datetime import date

from .client import Client
from .product import Product


class Reserve(NamedTuple):
    id: str
    product: Product
    client: Client
    reserve_date: date
    payment: float
    balance_due: float
