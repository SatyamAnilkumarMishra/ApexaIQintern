import requests
from app.cache import quote_cache

def getQuote():

    if "daily_quote" in quote_cache:
        return quote_cache["daily_quote"]

    url = "https://zenquotes.io/api/today"

    response = requests.get(url)

    if response.status_code != 200:
            return {"quote": "Keep pushing forward.", "author": "System"}
    
    data = response.json()[0]

    result = {
        "quote": data.get("q"),
        "author": data.get("a")
    }

    quote_cache["daily_quote"] = result

    return result