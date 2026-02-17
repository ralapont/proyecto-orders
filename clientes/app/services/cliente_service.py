from app.schemas.cliente_schema import ClienteCreate, ClienteResponse
from app.models.cliente_model import Cliente
from app.db.mongo import get_collection

COLLECTION = "clientes"

async def create_cliente(data: ClienteCreate) -> Cliente:
    collection = get_collection(COLLECTION)

    cliente_dict = data.model_dump()
    result = await collection.insert_one(cliente_dict)

    return Cliente(
        id = str(result.inserted_id),
        **cliente_dict
    )