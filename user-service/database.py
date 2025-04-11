# database.py
import os
import logging
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()
logging.info(f"DB USER: {os.getenv('POSTGRES_USER')}")
logging.info(f"DB PASSWORD: {os.getenv('POSTGRES_PASSWORD')}")
logging.info(f"DB HOST: {os.getenv('POSTGRES_HOST')}")
logging.info(f"DB PORT: {os.getenv('POSTGRES_PORT')}")
logging.info(f"DB NAME: {os.getenv('POSTGRES_DB')}")


DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@" \
               f"{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"

logging.basicConfig(level=logging.INFO)
logging.info(f"👉 Using DATABASE_URL: {DATABASE_URL}")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
