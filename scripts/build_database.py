"""
Run Script to build database:

load data
clean data
process data
store data in db

"""
import sys
from pathlib import Path

parent_path = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_path))

from config import *
from src.database import *
from src.data import *

def main():
    connection = db_connect()

    dfs = {
        instrument : load_and_clean(RAW_DATA_DIR / metadata['raw'], instrument)
        for instrument, metadata in INSTRUMENTS.items()
    }

    merged = merge_price_data(dfs).dropna()

    db_save_df(connection, merged, 'market_prices')

    connection.close()

if __name__ == "__main__":
    main()


