from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    MONGO_HOST: str = os.getenv("MONGO_HOST")
    MONGO_PORT: str = os.getenv("MONGO_PORT")
    MONGO_USER: str = os.getenv("MONGO_USER")
    MONGO_PASSWORD: str = os.getenv("MONGO_PASSWORD")
    MONGO_DB: str = os.getenv("MONGO_DB")

    @property
    def MONGO_URI(self):
        return (
            f"mongodb://{self.MONGO_USER}:{self.MONGO_PASSWORD}"
            f"@{self.MONGO_HOST}:{self.MONGO_PORT}/{self.MONGO_DB}"
        )

settings = Settings()