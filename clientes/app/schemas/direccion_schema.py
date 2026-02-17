from pydantic import BaseModel, Field

class Direccion(BaseModel):
    tipo_via: str = Field(..., min_length=1)
    nombre_via: str = Field(..., min_length=1)
    numero_via: str = Field(..., min_length=1)
    codigo_postal: str = Field(..., min_length=1)
    ciudad: str = Field(..., min_length=1)
    provincia: str = Field(..., min_length=1)
