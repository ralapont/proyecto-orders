from pydantic import BaseModel
from typing import Optional
from app.schemas.direccion_schema import Direccion

class Cliente(BaseModel):
    id: Optional[str]
    nombre: str
    email: str
    telefono: Optional[str]
    direccion: Direccion
