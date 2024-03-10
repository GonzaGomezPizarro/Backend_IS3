from pydantic import BaseModel
from typing import Optional


# Definir un modelo de usuario
class User(BaseModel):
    id: Optional[str]
    username: str #unique
    email: str
    info: str