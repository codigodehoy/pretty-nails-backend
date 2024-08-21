from typing import Optional

from domain.src.repositories import CategoryRepository
from domain.src.models import Category

class MemoryCategoryRepository(CategoryRepository):
    def __init__(self) -> None:
        self.category = []

    def create_category(self, category: Category) -> Category:
        id = f"CATEGORY#{category.id}"
        item = {"PK": id, "SK": id, "category_name": category.category_name}
        self.category.append(item)
        return category

    def get_category_by_id(self, category_id: str) -> Optional[Category]:
        raise NotImplemented
