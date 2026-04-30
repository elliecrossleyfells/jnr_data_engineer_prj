from fetch_data import get_apple_stock
from database import create_db, insert_data

# get apple stock data from the function defined in fetch_data.py
data = get_apple_stock() 
create_db()
insert_data(data)
print(data)

