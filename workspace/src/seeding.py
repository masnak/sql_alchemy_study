# src/seeding.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import random
import string

# Database connection
engine = create_engine('sqlite:///your_database.db')
Session = sessionmaker(bind=engine)
session = Session()

# Sample data for orders
for _ in range(10):
    order = orders.insert().values(
        order_id=random.randint(1, 100),
        user_id=random.randint(1, 10),
        product_id=random.randint(1, 10),
        quantity=random.randint(1, 10),
        unit_cost=float(random.randint(100, 1000))
    )
    session.execute(order)

# Sample data for users
for _ in range(10):
    user = users.insert().values(
        user_id=random.randint(1, 100),
        username=''.join(random.choices(string.ascii_uppercase + string.digits, k=15)),
        email_address=''.join(random.choices(string.ascii_uppercase + string.digits, k=10)) + "@example.com",
        phone=''.join(random.choices(string.digits, k=10)),
        password=''.join(random.choices(string.ascii_uppercase + string.digits, k=25)),
        created_on=datetime.now(),
        updated_on=datetime.now()
    )
    session.execute(user)

# Commit the changes
session.commit()