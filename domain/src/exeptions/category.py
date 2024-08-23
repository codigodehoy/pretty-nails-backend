class CategoryNameAlreadyExistsException(Exception):
    def __init__(self, category_name: str):
        message = f"The category name: '{category_name}' already exists."
        super().__init__(message)
