from sqlalchemy.sql import select
from create_tables import cookies, connection

s = cookies.select()
rp = connection.execute(s)
results = rp.fetchall()

print(results)