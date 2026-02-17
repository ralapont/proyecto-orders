from pydantic import BaseModel, Field
from typing import Optional
from .direccion_schema import Direccion

class ClienteCreate(BaseModel):
    nombre: str = Field(..., min_length = 1)
    email: str
    telefono: Optional[str] = None
    direccion: Direccion

class ClienteResponse(ClienteCreate):
    id: str