class CategoryAlreadyExistsException(Exception):
    def __init__(self, entity_type: str, entity_name: str):
        message = f"The {entity_type} with the name '{entity_name}' already exists."
        super().__init__(message)
