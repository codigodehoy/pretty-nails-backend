from domain.src.models import Category
from domain.src.repositories import CategoryRepository

class CreateCategory:

    def __init__(self, respository_category: CategoryRepository) -> None:
        self.respository_category = respository_category
    
    def main(self, request: Category):        
        return self.respository_category.create_category(request)
