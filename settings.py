import os
from dotenv import load_dotenv


load_dotenv()

DB_HOST = os.getenv('POSTGRES_HOST')
DB_PORT = os.getenv('POSTGRES_PORT')
DB_USER = os.getenv('POSTGRES_USER')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
AUTH_TOKEN_SECRET = os.getenv('AUTH_TOKEN_SECRET')
