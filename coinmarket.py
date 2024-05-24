import requests

def get_crypto_price(symbol, currency='USDT'):
    url = 'https://min-api.cryptocompare.com/data/price'
    params = {
        'fsym': symbol.upper(),
        'tsyms': currency.upper()
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Check for HTTP request errors
        data = response.json()
        if currency.upper() in data:
            return data[currency.upper()]
        else:
            return f"Currency '{currency}' not found in the response."
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"