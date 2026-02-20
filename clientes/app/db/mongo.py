from motor.motor_asyncio import AsyncIOMotorClient
from app.config.settings import settings

client = AsyncIOMotorClient(settings.MONGO_URI)
db = client[settings.MONGO_DB]

def get_collection(name: str):
    print(">>> URI:", settings.MONGO_URI)
    return db[name]