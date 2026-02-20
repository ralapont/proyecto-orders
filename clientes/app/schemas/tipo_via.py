from enum import Enum

class TipoVia(str, Enum):
    CALLE = "calle"
    AVENIDA = "avenida"
    PASEO = "paseo"
    CARRETERA = "carretera"
    PLAZA = "plaza"