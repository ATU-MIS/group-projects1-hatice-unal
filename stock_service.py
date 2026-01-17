import requests

STOCK_ENDPOINT = "https://www.alphavantage.co/query"

def check_stock_discount(stock_symbol, threshold, api_key):
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock_symbol,
        "apikey": api_key,
    }

    response = requests.get(STOCK_ENDPOINT, params=params, timeout=10)
    data = response.json()

    if "Time Series (Daily)" not in data:
        return None

    daily_data = list(data["Time Series (Daily)"].values())

    yesterday_close = float(daily_data[0]["4. close"])
    day_before_close = float(daily_data[1]["4. close"])

    difference = day_before_close - yesterday_close
    percentage_change = (difference / day_before_close) * 100

    if percentage_change >= threshold:
        return {
            "symbol": stock_symbol,
            "discount": round(percentage_change, 2),
            "price": yesterday_close
        }

    return None

def get_current_price(stock_symbol, api_key):
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": stock_symbol,
        "apikey": api_key
    }

    response = requests.get(url, params=params, timeout=10)
    data = response.json()

    try:
        return float(data["Global Quote"]["05. price"])
    except:
        return None

