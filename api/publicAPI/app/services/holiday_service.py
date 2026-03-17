import requests
from app.cache import holiday_cache


def getHolidays(country,year):
    country_code = country.upper()
    cache_key=f"{country_code}-{year}"

    if cache_key in holiday_cache:
        return holiday_cache[cache_key]
    
    url = f"https://date.nager.at/api/v3/PublicHolidays/{year}/{country_code}"
    response=requests.get(url)

    if response.status_code == 204:
        return {"message": f"No holidays found for {country_code} in {year}.", "holidays": []}
    
    if response.status_code != 200:
        return {"error": "API Error", "status": response.status_code}
    
    data=response.json()

    holidays=[]
    for h in data:
        holidays.append({
            "name": h.get("localName"),
            "date": h.get("date"),
            "country": country_code,    
            "type":h.get("types")
        })
    holiday_cache[cache_key]=holidays
    return holidays