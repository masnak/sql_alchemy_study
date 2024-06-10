# workspace/src/test1.py

from datetime import datetime
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Numeric, DateTime

metadata = MetaData()

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

users = Table('users', metadate,
    Column('user_id', Integer(), primary_key=True),
    Column('username', String(15), nullable=False, unique=True),
    Column('email_address', String(255), nullable=False),
    Column('phone', String(20), nullable=False),
    Column('password', String(25), nullable=False),
    Column('created_on', DateTime(), default=datetime.now),
    Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
)



# Create the table in the database
metadata.create_all(engine)