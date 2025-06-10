import duckdb 
from constants import DATA_WAREHOUSE_PATH

def query_dwh(query: str = "SELECT * FROM marts.mart_technical_jobs"):
    with duckdb.connect(DATA_WAREHOUSE_PATH) as conn:
        return conn.query(query).df()