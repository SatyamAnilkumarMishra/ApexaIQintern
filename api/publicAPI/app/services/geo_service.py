import requests
from app.cache import geo_cache

def get_ip_location(ip: str):

    if ip in geo_cache:
        return geo_cache[ip]

    url = f"http://ip-api.com/json/{ip}"

    response = requests.get(url)
    if response.status_code !=200:
        return {"error":"Something went wrong"}
    
    data = response.json()

    if data["status"] != "success":
        return {"error": "Invalid IP address"}

    result = {
        "ip": ip,
        "country": data["country"],
        "region": data["regionName"],
        "city": data["city"],
        "latitude": data["lat"],
        "longitude": data["lon"],
        "isp": data["isp"]
    }

    geo_cache[ip] = result
    return result