from flask import Flask, render_template
import sqlite3 as sq
import pandas as pd

app = Flask(__name__) #create web app

DB = "apple_stock_202604.db"
TABLE = "apple_stock_data_202604"

@app.route("/") # when homepage visited, run the below = the root URL (e.g. http://127.0.0.1:5000/)
def home():
    conn = sq.connect(DB)

    df = pd.read_sql_query(
        f"SELECT * FROM {TABLE}",
        conn
    )

    conn.close()

    # send data to html webpage and render a template
    return render_template(
        "index.html",
        tables = df.to_html(classes="stock_table", index=False), # classes allows CSS styling
        title="Apple Stock Data April 2026"
    )

#UN COMMENT IF WANT TO LAUNCH LOCALLY 
#if __name__ == "__main__":
    #app.run(debug=True) #allow error messages

# launch in docker 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
