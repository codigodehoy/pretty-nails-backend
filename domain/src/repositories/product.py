from abc import ABC, abstractmethod
from typing import Optional

from ..models import Product


class ProductRepository(ABC):

    @abstractmethod
    def create_product(self, product: Product) -> Product:
        raise NotImplemented
    
    @abstractmethod
    def update_product(self, product: Product) -> Product:
        raise NotImplemented
    
    @abstractmethod
    def get_all_products(self) -> list[Product]:
        raise NotImplemented
    
    @abstractmethod
    def get_product_by_id(self, product_id: str) -> Optional[Product]:
        raise NotImplemented
    
    @abstractmethod
    def get_products_by_category_name(self, category_name: str) -> Optional[Product]:
        raise NotImplemented
    
    @abstractmethod
    def delete_products(self, product_id: str) -> Optional[Product]:
        raise NotImplemented
