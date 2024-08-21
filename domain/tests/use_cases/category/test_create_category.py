from adapters.src.repository import MemoryCategoryRepository
from domain.src.use_cases import CreateCategory
from domain.src.models import Category


class TestCategoryUseCase:

    def test_should_create_a_category_sucessfuly(self):
        memory_category_repository = MemoryCategoryRepository()
        create_use_case = CreateCategory(respository_category=memory_category_repository)
        request = Category(id="12345678-1234-567812345678", category_name="Minimalist Designs")

        response = create_use_case.main(request)

        assert response == request
