from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

RAW_DATA_DIR = PROJECT_ROOT / 'data' / 'raw'
PROCESSED_DATA_DIR = PROJECT_ROOT / 'data' / 'processed'
TABLES_DIR = PROJECT_ROOT / 'outputs' / 'tables'
FIGURES_DIR = PROJECT_ROOT / 'outputs' / 'figures'
DATABASE_PATH = PROJECT_ROOT / 'data' / 'commodity_data.duckdb'

## Dates
START_DATE = '2016-06-01'
END_DATE = '2026-06-30'

## Instruments
INSTRUMENTS = {
    'WTI' : {
        'ticker' : 'CL',
        'units' : 'USD/barrel',
        'raw' : 'wti.csv'
    },
    'BRENT' : {
        'ticker' : 'LCO',
        'units' : 'USD/barrel',
        'raw' : 'brent.csv'
    },
    'GASOLINE' : {
        'ticker' : 'GPR',
        'units' : 'USD/gallon',
        'raw' : 'gasoline.csv'
    },
    'HEATING_OIL' : {
        'ticker' : 'NYF',
        'units' : 'USD/gallon',
        'raw' : 'heating_oil.csv'
    }
}

if __name__ == '__main__':
    for directory in [
        RAW_DATA_DIR,
        PROCESSED_DATA_DIR,
        TABLES_DIR,
        FIGURES_DIR
    ]:
        directory.mkdir(parents=True, exist_ok=True)