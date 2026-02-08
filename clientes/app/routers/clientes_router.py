from fastapi import APIRouter
from app.schemas.cliente_schema import Cliente
from app.services.cliente_service import obtener_clientes

router = APIRouter()

@router.get("/", response_model=list[Cliente])
def listar_clientes():
    return obtener_clientes()