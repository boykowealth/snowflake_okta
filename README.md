# SnowFlake Connector
_SnowFlake Server Connector From Okta Verification_

# Snowflake Connector README

## Overview
This Python script provides a simple way to connect to a Snowflake database using the `snowflake-connector-python` library and execute SQL queries, returning results as a pandas DataFrame.

## Requirements
- Python 3.x
- `pandas`
- `snowflake-connector-python`

## Installation
```bash
pip install pandas snowflake-connector-python
```

## Usage
### Import the module
```python
from your_script_name import SNOW
```

### Execute a SQL query
```python
sql_1 = """
SELECT
    a.MATERIAL,
    a.ITEM_BASE_UOM AS BASE_UOM,
    a.LISTPRICEPER AS LIST_PRICE_PER
FROM
    EXAMPLE AS a
WHERE
    a.LISTPRICEPER IS NOT NULL
"""

SNOW.execute("your_user_id", "your_database", "your_warehouse", sql_1)
```

## Code Explanation
### Class and Method
```python
class SNOW():
    def execute(ID, DATABASE, WAREHOUSE, SQL):
```
- `ID`: User ID for Snowflake login.
- `DATABASE`: The Snowflake database to connect to.
- `WAREHOUSE`: The Snowflake warehouse to use.
- `SQL`: The SQL query to execute.

### Connection
```python
ctx = snow.connect(
    authenticator='externalbrowser',
    user=ID,
    host="host_url",
    account="account_name",
    database=DATABASE,
    warehouse=WAREHOUSE,
    login_timeout=60,
    network_timeout=30,
    socket_timeout=10
)
```
- The script establishes a connection using external browser authentication.

### Fetching Results
```python
with ctx.cursor() as cursor:
    cursor.execute(SQL)
    columns = [col[0] for col in cursor.description]
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=columns)
    print(df)
```
- The results are fetched into a Pandas DataFrame and printed.

### Exception Handling
```python
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    ctx.close()
```
- Exceptions are caught and the connection is closed properly.

## Author
Brayden Boyko

## Disclaimer
Ensure you have the required permissions and credentials to access the Snowflake database securely.
