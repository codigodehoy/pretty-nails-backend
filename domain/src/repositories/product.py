from abc import ABC, abstractmethod
from typing import Optional

from models import Product


class ProductRepository(ABC):

    @abstractmethod
    def create(self, product: Product) -> Product:
        raise NotImplemented
    
    @abstractmethod
    def update(self, product: Product) -> Product:
        raise NotImplemented
    
    @abstractmethod
    def get_all(self) -> list[Product]:
        raise NotImplemented
    
    @abstractmethod
    def get_by_id(self, product_id: str) -> Optional[Product]:
        raise NotImplemented
    
    @abstractmethod
    def delete(self, product_id: str) -> Optional[Product]:
        raise NotImplemented
