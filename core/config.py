import os
from dotenv import load_dotenv

from pathlib import Path  # python3 only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)



class Settings:
    PROJECT_NAME: str = "Lendza"
    PROJECT_VERSION: str = "0.1.1"
    
    POSTGRES_USER : str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER","localhost")
    POSTGRES_PORT : str = os.getenv("POSTGRES_PORT",5432) # default postgres port is 5432
    POSTGRES_DB : str = os.getenv("POSTGRES_DB","tdd")
    SECRET_KEY :str = os.getenv("SECRET_KEY")   
    ALGORITHM = "HS256"                         
    ACCESS_TOKEN_EXPIRE_MINUTES = 1440
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

settings = Settings()