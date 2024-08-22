import pytest

from adapters.src.repository import MemoryCategoryRepository
from domain.src.use_cases import CreateCategory
from domain.src.models import Category
from domain.src.exeptions import CategoryAlreadyExistsException


class TestCategoryUseCase:

    def test_should_create_a_category_sucessfuly(self):
        memory_category_repository = MemoryCategoryRepository()
        create_use_case = CreateCategory(repository_category=memory_category_repository)
        request = Category(id="12345678-1234-567812345678", category_name="Minimalist Designs")

        response = create_use_case.main(request)

        assert response == request

    def test_should_raise_an_error_when_category_exist(self):
        expected_response = f"The {Category.__name__} with the name 'Minimalist Designs' already exists."
        memory_category_repository = MemoryCategoryRepository()
        create_use_case = CreateCategory(repository_category=memory_category_repository)
        request = Category(id="12345678-1234-567812345678", category_name="Minimalist Designs")
        create_use_case.main(request)

        with pytest.raises(CategoryAlreadyExistsException) as message_error:
            create_use_case.main(request)

        assert str(message_error.value) == expected_response
