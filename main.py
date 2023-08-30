from pandas import read_csv
from services import get_candles_ohlc, calc_ema, save_candles_with_ema_plot


if __name__ == '__main__':
    df = read_csv('prices.csv', index_col='TS', parse_dates=True)
    candles = get_candles_ohlc(df)

    ema_periods = 14
    ema = calc_ema(candles['Close'], ema_periods)

    start_plot_index, end_plot_index = 0, 200
    save_candles_with_ema_plot(candles, ema, start_plot_index, end_plot_index)
