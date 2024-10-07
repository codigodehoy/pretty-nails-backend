from domain.src.use_cases import CreateCategory
from adapters.src.repository import MemoryCategoryRepository

dummy_repository_category = MemoryCategoryRepository()

def create_category_factory():
    return CreateCategory(repository_category=dummy_repository_category)
