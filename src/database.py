import pandas as pd
import duckdb as ddb
import sys
from pathlib import Path

parent_path = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_path))

from config import *

def db_connect(database_path: Path = DATABASE_PATH):
    return ddb.connect(str(database_path))

## Saves DF into DB //TO DO:: make it more generalised
def db_save_df(connection: ddb.DuckDBPyConnection, df: pd.DataFrame, table_name: str) -> None:
    connection.register('df', df)

    connection.execute(f"""
        CREATE OR REPLACE TABLE {table_name} AS 
                       SELECT *
                       FROM df;
        
    """)

def db_query(connection: ddb.DuckDBPyConnection, query: str) -> pd.DataFrame:
    return connection.execute(query).df()

def db_query_file(connection: ddb.DuckDBPyConnection, file: str) -> pd.DataFrame:
    query = Path(file).read_text()
    return db_query(connection, query)