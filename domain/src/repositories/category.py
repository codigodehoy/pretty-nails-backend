from abc import ABC, abstractmethod
from typing import Optional

from ..models import Category

class CategoryRepository(ABC):

    @abstractmethod
    def create_category(self, category: Category) -> Category:
        raise NotImplemented
    
    @abstractmethod
    def get_category_by_id(self, category_id: str) -> Optional[Category]:
        raise NotImplemented
