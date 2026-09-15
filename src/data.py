import pandas as pd
from pathlib import Path
import sys
import pandas as pd
from functools import reduce

parent_path = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_path))

from config import *



## Merges price data from multiple different
def merge_price_data(dfs: dict[str, pd.DataFrame]) -> pd.DataFrame:

    for instrument, df in dfs.items():
        if df['date'].duplicated().any():
            raise ValueError(
                f'{instrument} contains duplicated dates'
            )
        
    main_df = reduce(
        lambda left, right: pd.merge(
            left, 
            right, 
            how='outer', 
            on='date'
        ), 
        dfs.values())

    main_df = (main_df
    .sort_values('date')
    .reset_index(drop=True))
    
    return main_df



def load_and_clean(file_path, instrument) -> pd.DataFrame:
    df = pd.read_csv(file_path)

    df = df.rename(columns={
        'Date' : 'date',
        'Price' : 'close'
    })

    df = df[['date', 'close']].copy()

    df = df.drop_duplicates()

    df['date'] = pd.to_datetime(df['date'])
    df['close'] = pd.to_numeric(df['close'])

    df = df[
            (df['date'] >= pd.to_datetime(START_DATE)) &
            (df['date'] <= pd.to_datetime(END_DATE))
           ]
    
    df = df.sort_values('date').reset_index(drop=True)

    df = df.rename(columns={
        'close' : instrument
    })

    return df

