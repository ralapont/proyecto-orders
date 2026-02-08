from fastapi import FastAPI
from app.routers.clientes_router import router as clientes_router
from app.config import settings


app = FastAPI(title="Servicio de Clientes")

@app.get("/debug/env")
def debug_env():
    return {
        "mongo_uri": settings.MONGO_URI,
        "mongo_db": settings.MONGO_DB
    }


app.include_router(clientes_router, prefix="/clientes", tags=["Clientes"])