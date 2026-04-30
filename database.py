import sqlite3 as sq
import pandas as pd

def create_db():
    connection = sq.connect("apple_stock_202604.db") # connect to db, if doesn't exist, will create. 
    cursor = connection.cursor() # cursor retrieves/manipulates data, add rows etc with SQL. 

# below sets up the table, assigning dtypes for each column in the apple stock data.
# id is included for a unique row identifier. 
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS apple_stock_data_202604 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Date TEXT,
        Open REAL,
        High REAL,
        Low REAL,
        Close REAL,
        Volume INTEGER,
        Dividends REAL,
        "Stock Splits" REAL
        )
        """)
    connection.commit() # save changes
    connection.close() # close db connection

# INSERT DATA 
def insert_data(data):
    if isinstance(data.index, pd.DatetimeIndex):
        data = data.reset_index()

    conn = sq.connect("apple_stock_202604.db")

    # assign apple stock data to db
    data.to_sql(
        "apple_stock_data_202604",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()




