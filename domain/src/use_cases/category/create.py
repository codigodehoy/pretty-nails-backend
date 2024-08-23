from domain.src.models import Category
from domain.src.repositories import CategoryRepository
from domain.src.exeptions import CategoryNameAlreadyExistsException


class CreateCategory:

    def __init__(self, repository_category: CategoryRepository) -> None:
        self.repository_category = repository_category
    
    def main(self, request: Category):
        category = self.repository_category.get_category_by_name(request.category_name)

        if category:
            raise CategoryNameAlreadyExistsException(category_name=request.category_name)

        response = self.repository_category.create_category(request)
        return response
