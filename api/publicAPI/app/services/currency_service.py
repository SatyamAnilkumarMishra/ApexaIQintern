import requests
from app.cache import currency_cache
from app.config import setting

API_KEY=setting.EXCHANGE_API

def currencyConverter(from_currency, to_currency, amount):
    cache_key=f"{from_currency}"
    if cache_key in currency_cache:
        rates=currency_cache[cache_key]
    else:
        url=f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"
        response=requests.get(url)
        data=response.json()

        rates=data["conversion_rates"]
        currency_cache[cache_key]=rates
    
    if to_currency not in rates:
        return {"error":"Invalid target currency"}
    rate=rates[to_currency]
    converted_amount=amount*rate

    return{
        "from": from_currency,
        "to": to_currency,
        "amount": amount,
        "exchange_rate": rate,
        "converted_amount": round(converted_amount, 2)
    }
