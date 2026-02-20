from pydantic import BaseModel, Field, EmailStr
from .direccion_schema import Direccion

class ClienteCreate(BaseModel):
    nombre: str = Field(
        ... ,
        min_length = 1,
        description = "Nombre completo del cliente",
        example = "Juan Pérez"
    )

    email: EmailStr = Field(
        ...,
        description="Correo electrónico válido del cliente",
        example="juan.perez@example.com"
    )

    telefono: str | None = Field(
        None,
        description="Número de teléfono del cliente (opcional)",
        example="+34 600 123 456"
    )

    direccion: Direccion

    class Config:
        json_schema_extra = {
            "example": {
                "nombre": "Juan Pérez",
                "email": "juan.perez@example.com",
                "direccion": {
                    "tipo_via": "Calle",
                    "nombre_via": "Gran Vía",
                    "numero_via": "45",
                    "codigo_postal": "28013",
                    "ciudad": "Madrid",
                    "provincia": "Madrid"
                }
            }
        }

class ClienteResponse(ClienteCreate):
    id: str = Field(
        ...,
        description = "Identificador único del cliente en la base de datos",
        example = "65b1f8e2c9a1"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "id": "65b1f8e2c9a1",
                "nombre": "Juan Pérez",
                "email": "juan.perez@example.com",
                "direccion": {
                    "tipo_via": "Calle",
                    "nombre_via": "Gran Vía",
                    "numero_via": "45",
                    "codigo_postal": "28013",
                    "ciudad": "Madrid",
                    "provincia": "Madrid"
                }
            }
        }

