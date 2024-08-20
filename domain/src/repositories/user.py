from abc import ABC, abstractmethod
from typing import Optional

from ..models import User


class UserRepository(ABC):

    @abstractmethod
    def get_user_by_email(self, user_email) -> Optional[User]:
        raise NotImplemented
