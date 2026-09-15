import pandas as pd
import numpy as np

def calculate_simple_returns(price: pd.Series) -> pd.Series:
    return price.pct_change()

def calculate_log_returns(price: pd.Series) -> pd.Series:
    return np.log(price / price.shift(1))

def calculate_cumulative_returns(returns: pd.Series) -> pd.Series:
    return (1 + returns).cumprod() - 1

def calculate_cumulative_log_returns(returns: pd.Series) -> pd.Series:
    # Need to change back to simple returns
    return returns.cumsum()