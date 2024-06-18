from sqlalchemy import create_engine
from create_tables import cookies, users, orders, line_items

engine = create_engine('postgresql+psycopg2://docker:docker@localhost:5432/docker')
connection = engine.connect()

ins = cookies.insert().values(
    cookie_name="chocolate chip",
    cookie_recipe_url="http://some.aweso.me/cookie/recipe.html",
    cookie_sku="CC01",
    quantity="12",
    unit_cost="0.50"
)
print(str(ins))

result = connection.execute(ins)