from fastapi import APIRouter, Depends

from uuid import uuid4

from factories.use_cases import create_category_factory
from domain.src.models import Category
from ..dtos import CategoryRequest

category = APIRouter()


@category.post("/")
def create_category(request: CategoryRequest, use_case=Depends(create_category_factory)):
    category_id = uuid4()
    category = Category(id=category_id, category_name=request.category_name)
    response = use_case.main(category)
    return response._asdict()
