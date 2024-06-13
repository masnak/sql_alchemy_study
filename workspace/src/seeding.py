# workspace/src/seeding.py

from datetime import datetime
from sqlalchemy import create_engine, insert
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from create_tables import cookies, users

# create engine
engine = create_engine('postgresql+psycopg2://docker:docker@localhost:5432/docker', client_encoding='utf8')

# create session
Session = sessionmaker(bind=engine)
session = Session()

try:
    # insert sample data into cookies table
    print("Inserting data into cookies table...")
    session.execute(insert(cookies), [
        {'cookie_id': 1, 'cookie_name': 'チョコチップ', 'cookie_recipe_url': 'http://example.com/cookies/choco_chip', 'cookie_sku': 'CC01', 'quantity': 50, 'unit_cost': 0.50},
        {'cookie_id': 2, 'cookie_name': 'ショートブレッド', 'cookie_recipe_url': 'http://example.com/cookies/shortbread', 'cookie_sku': 'SB01', 'quantity': 75, 'unit_cost': 0.60},
        {'cookie_id': 3, 'cookie_name': 'オートミール', 'cookie_recipe_url': 'http://example.com/cookies/oatmeal', 'cookie_sku': 'OM01', 'quantity': 80, 'unit_cost': 0.70},
        {'cookie_id': 4, 'cookie_name': 'ピーナッツバター', 'cookie_recipe_url': 'http://example.com/cookies/peanut_butter', 'cookie_sku': 'PB01', 'quantity': 90, 'unit_cost': 0.80},
        {'cookie_id': 5, 'cookie_name': 'シュガークッキー', 'cookie_recipe_url': 'http://example.com/cookies/sugar', 'cookie_sku': 'SC01', 'quantity': 100, 'unit_cost': 0.90},
    ])
    print("Data inserted into cookies table successfully.")
    session.commit()
except SQLAlchemyError as e:
    print(f"Error inserting data into cookies table: {e}")
    session.rollback()

try:
    # insert sample data into users table
    print("Inserting data into users table...")
    session.execute(insert(users), [
        {'user_id': 1, 'username': 'user1', 'email_address': 'user1@example.com', 'phone': '123-456-7890', 'password': 'password1', 'created_on': datetime.now(), 'updated_on': datetime.now()},
        {'user_id': 2, 'username': 'user2', 'email_address': 'user2@example.com', 'phone': '234-567-8901', 'password': 'password2', 'created_on': datetime.now(), 'updated_on': datetime.now()},
        {'user_id': 3, 'username': 'user3', 'email_address': 'user3@example.com', 'phone': '345-678-9012', 'password': 'password3', 'created_on': datetime.now(), 'updated_on': datetime.now()},
        {'user_id': 4, 'username': 'user4', 'email_address': 'user4@example.com', 'phone': '456-789-0123', 'password': 'password4', 'created_on': datetime.now(), 'updated_on': datetime.now()},
        {'user_id': 5, 'username': 'user5', 'email_address': 'user5@example.com', 'phone': '567-890-1234', 'password': 'password5', 'created_on': datetime.now(), 'updated_on': datetime.now()},
    ])
    print("Data inserted into users table successfully.")
    session.commit()
except SQLAlchemyError as e:
    print(f"Error inserting data into users table: {e}")
    session.rollback()
finally:
    session.close()