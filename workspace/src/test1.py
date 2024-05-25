# workspace/src/test1.py

# create db session using sqlalchemy and postgresql+psycopg2 driver
from sqlalchemy import create_engine

# create engine
engine = create_engine('postgresql+psycopg2://docker:docker@localhost:5432/docker')

# create session
connection = engine.connect()