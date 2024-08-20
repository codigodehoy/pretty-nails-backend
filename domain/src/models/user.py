from typing import NamedTuple


class User(NamedTuple):
    id: str
    first_name: str
    last_name: str
    email: str
    movil_number: str
    role: str
