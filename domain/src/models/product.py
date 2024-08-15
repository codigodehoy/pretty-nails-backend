from typing import NamedTuple

from .category import Category


class Product(NamedTuple):
    id: str
    category: Category
    product_name: str
    description: str
    price: float
    duration_minutes: int
    image_url: str
