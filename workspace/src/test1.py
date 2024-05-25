# workspace/src/test1.py

# create db session using sqlalchemy and postgresql+psycopg2 driver
from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import Metadata
from sqlalchemy import Table, Column, Integer, String, Numeric, ForeignKey

metadata = Metadata()

# create engine
engine = create_engine('postgresql+psycopg2://docker:docker@localhost:5432/docker')

# create session
connection = engine.connect()

# create table
cookies = Table('cookies', metadata,
    Column('cookie_id', Integer(), primary_key=True),
    Column('cookie_name', String(50), index=True),
    Column('cookie_recipe_url', String(255)),
    Column('cookie_sku', String(55)),
    Column('quantity', Integer()),
    Column('unit_cost', Numeric(12, 2))
)
