from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

class Settings:
    MONGO_URI: str = os.getenv("MONGO_URI")
    MONGO_DB: str = os.getenv("MONGO_DB")

settings = Settings()