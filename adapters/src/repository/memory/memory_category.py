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

    def get_category_by_id(self, category_id: str) -> Optional[Category]:
        id = f"CATEGORY#{category_id}"
        for category in self.categories:
            if category.get("PK") == id:
                return Category(id=category_id, category_name=category.get("category_name"))
        
        return None
