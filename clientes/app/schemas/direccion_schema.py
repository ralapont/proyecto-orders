from pydantic import BaseModel, Field

class Direccion(BaseModel):
    tipo_via: str = Field(
        ...,
        min_length = 1,
        description = "Tipo de vía (calle, avenida, paseo, carretera, etc.)",
        example = "Calle"
    )

    nombre_via: str = Field(
        ...,
        min_length = 1,
        description = "Nombre de la vía",
        example = "Gran Vía"
    )

    numero_via: str = Field(
        ...,
        min_length = 1,
        description = "Número de la vía",
        example = "45"
    )

    codigo_postal: str = Field(
        ...,
        min_length = 1,
        description = "Código postal",
        example = "28013"
    )

    ciudad: str = Field(
        ...,
        min_length = 1,
        description = "Ciudad",
        example = "Madrid"
    )

    provincia: str = Field(
        ...,
        min_length = 1,
        description = "Provincia",
        example = "Madrid"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "tipo_via": "Calle",
                "nombre_via": "Gran Vía",
                "numero_via": "45",
                "codigo_postal": "28013",
                "ciudad": "Madrid",
                "provincia": "Madrid"
            }
        }

