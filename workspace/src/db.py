import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

class Model(DeclarativeBase):
    pass

load_dotenv()

engine = create_engine('postgresql+psycopg2://docker:docker@localhost:5432/docker')