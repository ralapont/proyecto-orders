from fastapi import APIRouter, status
from app.schemas.cliente_schema import ClienteCreate, ClienteResponse
from app.services.cliente_service import create_cliente

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.post(
    "",
    response_model = ClienteResponse,
    status_code= status.HTTP_201_CREATED
)
async def create_cliente_endpoint(cliente: ClienteCreate):
    return await create_cliente(cliente)
