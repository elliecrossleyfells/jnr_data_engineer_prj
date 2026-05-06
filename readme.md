# Junior Data Engineer Project - Apple Stock Data

## Overview

This project implements a simple data pipeline that pulls Apple stock data from the public API yfinance. It then stores the data in a SQLite database, and displays it through a Flask web application. The project is then containerised using Docker to enable repeatable and easy deployment.

## Stack
<b>Programming Language</b>: `Python` - Chosen as it's open-source and readable.
<b>Database:</b> `SQLite` - Chosen as already installed in Python, requires no setup, portable. 
<b>Frontend:</b> `Flask` - Provides a simple web application framework.
<b>Deployment:</b> `Docker` - Free to download and use. 


The project follows the below structure <br>

<b>1. Data Ingestion</b>: The project pulls Apple stock data from the `yfinance` API. The `fetch_data()` function requests historical stock data for a specified date range (April 2026 in this case.)<br>

<b>2. Database Storage</b>: The pulled data is stored in a SQLite database using a defined schema that captures key stock attributes such as date, open, close, high, low, and volume. Most columns are stored as floats, with date being stored at text. This is something I would change later and reasons for this are detailed in the below section. `database.py` handles both table creation and data insertion. <br>

<b>3. Display Layer / Frontend</b>: A lightweight frontend is implemented using `Flask`. The webpage is customised using basic HTML and CSS. Some JS functions are used to display the live datetime for aesthetic purposes and better user experience. <br>

<b> 4. Deployment</b>: The project is containerised using `Docker` to ensure it can be run in a consistent and repeatable way. A Dockerfile defines the environment, installs dependencies, and executes both the data ingestion script and the `Flask` application. This allows a new user to run the entire pipeline with a single command, without needing to install Python or any dependencies locally.

---

## Architecture

The project follows a basic data engineering pipeline:

```text
Yahoo Finance API
        ↓
fetch_data.py (data ingestion)
        ↓
main.py (orchestration)
        ↓
database.py (storage logic)
        ↓
SQLite database
        ↓
app.py (Flask backend)
        ↓
index.html (frontend display)
```
---

## How to run this project

### Local
- Install dependencies (pip install -r requirements.txt)
- Run `main.py`
- Run `app.py`
- Data will be visible via the URL provided (http://127.0.0.1:5000)

### Docker (Recommended)
- Open the code and run the following commands in the terminal
- `docker build -t apple-stock-app .`
- `docker run -p 5000:5000 apple-stock-app` 
- Data will be visible via the URL provided (http://localhost:5000)
- To stop the project, run the following commands in the terminal
    `docker ps` (this will provide you with the container ID)
    `docker stop <container_id>`

---

## Limitations and Future Improvements

1. The `Date` column is stored as text and includes a timestamp. The reason for storing as text is that in SQLite, there is no true dedicated Date storage type and so best to store as text for now. For this project, the time part is unnecessary and could be removed. Storing this as a correct date type would improve clarity and compatibility with BI/vis tools and this can be done using pandas after the insert_data() step. 

2. Mixing pandas indexing with database indexing: Although I added an auto-incrementing `id` column in the DB schema, it is not retained on final output. This is due to using `to_sql(..., if_exists="replace")`, which overwrites the table. A better approach would be to append data while preserving the schema.

3. The stock ticker and date range dates are hardcoded. These should be made dynamic (using environment variables or a config file)

4. There is no error handling for API failures. This could be improved with exception handling.

5. The filter input on the frontend webpage does not currently function and included for aesthetic/demonstration purposes only!

6. Further testing with larger datasets (e.g. >10k rows) would help assess performance, runtime and identify optimisation opportunities.
