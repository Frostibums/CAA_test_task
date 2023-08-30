import pandas as pd
import pytest

from services import get_candles_ohlc, calc_ema


@pytest.fixture
def test_trades():
    trades = {
        'TS': pd.to_datetime(['2023-05-04 18:21:10',
                              '2023-05-04 18:21:15',
                              '2023-05-04 18:21:19',
                              '2023-05-04 18:21:21',
                              '2023-05-04 18:21:26',
                              '2023-05-04 18:21:28',
                              '2023-05-04 18:21:32',
                              '2023-05-04 18:21:35',
                              '2023-05-04 18:21:39']),
        'PRICE': [1875, 1877, 1876, 1871, 1880, 1875, 1800, 1802, 1835]
    }
    return pd.DataFrame(trades).set_index('TS')


@pytest.fixture
def test_candles_closes():
    candles_closes = {
        'TS': pd.to_datetime(['2023-05-04 18:21:10',
                              '2023-05-04 18:21:15',
                              '2023-05-04 18:21:19',
                              '2023-05-04 18:21:21',
                              '2023-05-04 18:21:26',
                              '2023-05-04 18:21:28',
                              '2023-05-04 18:21:32',
                              '2023-05-04 18:21:35',
                              '2023-05-04 18:21:39']),
        'Close': [1875, 1877, 1876, 1871, 1880, 1875, 1800, 1802, 1835]
    }
    return pd.DataFrame(candles_closes).set_index('TS')['Close']


def test_get_candles_ohlc(test_trades):
    test_candles = get_candles_ohlc(test_trades, '10S')

    # Проверка корректности агрегации
    assert len(get_candles_ohlc(test_trades, '1S')) == 30
    assert len(get_candles_ohlc(test_trades, '5S')) == 6
    assert len(get_candles_ohlc(test_trades, '10S')) == 3

    # Проверка агрегированных значений и наименования столбцов
    assert list(test_candles.columns) == ['Open', 'High', 'Low', 'Close']
    assert list(test_candles['Open']) == [1875, 1871, 1800]
    assert list(test_candles['High']) == [1877, 1880, 1835]
    assert list(test_candles['Low']) == [1875, 1871, 1800]
    assert list(test_candles['Close']) == [1876, 1875, 1835]


def test_calc_ema(test_candles_closes):
    periods = 6  # periods < len(test_candles_closes)
    ema = calc_ema(test_candles_closes, periods)

    # Проверка длины EMA
    assert len(ema) == len(test_candles_closes)
    assert len(ema.dropna()) == len(test_candles_closes) - periods + 1  # +1 тк в calc_ema мы задаем ema[periods - 1]



