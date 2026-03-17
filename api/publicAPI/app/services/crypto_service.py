from app.config import setting
import requests
from app.cache import crypto_cache


def priceTracker(coin: str, currency: str = "usd"):
    coin = coin.lower()
    currency = currency.lower()

    cache_key=f"{coin}-{currency}"
    if cache_key in crypto_cache:
        return crypto_cache[cache_key]
    
    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids": coin,
        "vs_currencies": currency
    }
    response=requests.get(url,params=params)
    data=response.json()

    if not data or coin not in data:
        return {"error": f"Coin '{coin}' not found on CoinGecko."}
    
    price = data[coin].get(currency)

    if price is None:
        return {"error": f"Currency '{currency}' not supported for this coin."}

    result = {
        "coin": coin,
        "currency": currency,
        "price": price
    }

    crypto_cache[cache_key] = result
    return result
