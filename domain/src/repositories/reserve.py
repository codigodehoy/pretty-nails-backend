from abc import ABC, abstractmethod
from datetime import datetime

from ..models import Reserve


class ReserveRepository(ABC):

    @abstractmethod
    def create_reserve(self, reserve: Reserve) -> Reserve:
        raise NotImplemented
    
    @abstractmethod
    def update_reserve(self, reserve: Reserve) -> Reserve:
        raise NotImplemented
    
    @abstractmethod
    def get_reserves_by_client_email(self, client_email: str) -> list[Reserve]:
        raise NotImplemented
    
    @abstractmethod
    def get_reserves_by_product(self, product_id: str) -> list[Reserve]:
        raise NotImplemented
    
    @abstractmethod
    def get_reserves_by_date(self, reserve_date: datetime) -> list[Reserve]:
        raise NotImplemented
    
    @abstractmethod
    def delete_reserve(self, reserve_id: str) -> list[Reserve]:
        raise NotImplemented
