import os

from dotenv import load_dotenv

load_dotenv()

PG_USER = os.getenv('PG_USER')
PG_PASSWORD = os.getenv('PG_PASSWORD')
PG_DB = os.getenv('PG_DB')
PG_HOST = os.getenv('PG_HOST')
PG_PORT = os.getenv('PG_PORT')

DATABASE_URL = f'postgresql+asyncpg://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}'
