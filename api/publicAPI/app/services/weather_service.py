import requests
from app.cache import weather_cache
from app.config import setting

API_KEY = setting.WEATHER_API

def get_weather(city):

    if city.lower() in weather_cache:
        return weather_cache[city.lower()]

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": response.get("message", "API Error"), "status": response.status_code}
    
    res = response.json()
    data = {
        "city": city,
        "temperature": res["main"]["temp"],
        "humidity": res["main"]["humidity"],
        "description": res["weather"][0]["description"]
    }

    weather_cache[city] = data
    return data