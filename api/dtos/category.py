from pydantic import BaseModel

class CategoryRequest(BaseModel):
    category_name: str
