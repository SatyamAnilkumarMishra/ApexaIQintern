import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    WEATHER_API=os.getenv("WEATHER_API")
    OMDB_API=os.getenv("OMDB_API")
    NEWS_API=os.getenv("NEWS_API")
    EXCHANGE_API=os.getenv("EXCHANGE_API")
    NAGER_API=os.getenv("NAGER_API")
setting=Settings()