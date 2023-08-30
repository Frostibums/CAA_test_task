# Test assignment for a vacancy Middle-Level Python Developer (Cryptocurrency Trading Bot)
Task: Create a Candlestick Chart and Calculate the Exponential Moving Average (EMA)

## Usage
1. Clone this repository using following comand:
```sh
git clone https://github.com/your-username/candlestick-ema.git
```

2. Navigate to the project directory:
```sh
cd candlestick-ema
```

3. Install all required dependencies:
```sh
pip install -r requirements.txt
```

4. Run the main script:
```sh
python main.py
```

## Functionality
- `main.py`: The main script that reads trade data from `prices.csv`, aggregates it into candlesticks, calculates EMA, and saves the candlestick chart with EMA as candles_with_ema.png.
- `services.py`: Contains functions to aggregate trade data into candlesticks, EMA calculation function and plot saving function.
- `test.py`: Unit tests for candlestick aggregation and EMA calculation functions.

## How to Run Tests
Run the tests using pytest:
```sh
pytest test.py
```

## Results
The program will save the candlestick chart with the EMA for the specified period as candles_with_ema.png.
