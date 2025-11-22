import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', '12345678')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '3306')
DB_NAME = os.getenv('DB_NAME', 'sixt_development')

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

ECHO_SQL = os.getenv('SQLALCHEMY_ECHO', 'false').lower() == 'true'

db = SQLAlchemy()
