from domain.src.models import Category
from domain.src.repositories import CategoryRepository
from domain.src.exeptions import CategoryAlreadyExistsException


class CreateCategory:

    def __init__(self, repository_category: CategoryRepository) -> None:
        self.repository_category = repository_category
    
    def main(self, request: Category):
        category = self.repository_category.get_category_by_id(request.id)

        if category and request.category_name == category.category_name:
            raise CategoryAlreadyExistsException(entity_type=Category.__name__, entity_name=request.category_name)

        return self.repository_category.create_category(request)
