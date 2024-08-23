from typing import Optional

from domain.src.repositories import CategoryRepository
from domain.src.models import Category

class MemoryCategoryRepository(CategoryRepository):
    def __init__(self) -> None:
        self.categories = []

    def create_category(self, category: Category) -> Category:
        category_id = f"CATEGORY#{category.id}"
        item = {"PK": category_id, "SK": category_id, "category_name": category.category_name}
        self.categories.append(item)
        return category

    def get_category_by_name(self, category_name: str) -> Optional[Category]:
        for category in self.categories:
            if category.get("category_name") == category_name:
                category_id = category.get("PK")
                return Category(id=category_id, category_name=category_name)
        
        return None

    def get_category_by_id(self, category_id: str) -> Optional[Category]:
        raise NotImplemented
