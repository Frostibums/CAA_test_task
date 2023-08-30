from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd
import mplfinance as mpf


def get_candles_ohlc(df: pd.DataFrame, period: str = '1H') -> pd.DataFrame:
    """Aggregate trades data into OHLC candlesticks."""
    rename_map = {
        'first': 'Open',
        'max': 'High',
        'min': 'Low',
        'last': 'Close',
    }

    resampled_df = df.resample(period).agg(['first', 'max', 'min', 'last'])  # aggregating trades into candlesticks
    resampled_df.columns = resampled_df.columns.droplevel(0)
    return resampled_df.rename(columns=rename_map)


def calc_ema(df: pd.Series, periods: int = 1) -> pd.Series:
    """Calculate Exponential Moving Average (EMA) for a DataFrame column."""
    k = 2 / (periods + 1)  # smoothing constant
    ema = pd.Series(index=df.index)
    ema[periods - 1] = df[:periods].mean()  # since EMA is calculated based on the number of periods
    for i in range(periods, len(df)):
        ema.iloc[i] = (df.iloc[i] - ema.iloc[i - 1]) * k + ema.iloc[i - 1]  # formula for calculating EMA
    return ema


def save_candles_with_ema_plot(df: pd.DataFrame, ema: pd.Series, start_pos: int, end_pos: int) -> None:
    """Save candlestick chart with Exponential Moving Average (EMA) as candles_with_ema.png"""
    mpf.plot(df[start_pos:end_pos],
             type='candle',
             style='yahoo',
             addplot=[mpf.make_addplot(ema[start_pos:end_pos])],
             savefig='candles_with_ema.png')
