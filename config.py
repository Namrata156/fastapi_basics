from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "postgresql://postgres:namrata@localhost:5432/FastAPI_data"
engine = create_engine(db_url)
session = sessionmaker(autoflush=False,autocommit=False,bind=engine)
