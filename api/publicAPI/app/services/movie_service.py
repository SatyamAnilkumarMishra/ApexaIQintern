import requests
from app.config import setting

def search_Movies(query,page:int=1):
    url=f"http://www.omdbapi.com/?apikey={setting.OMDB_API}&s={query}&page={page}"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "API Connection Failed", "status": response.status_code}
    
    res = response.json()

    if res.get("Response") == "False":
        return {"error": res.get("Error", "Movie not found"), "totalResults": "0"}
    
    return {
        "results": res.get("Search", []),
        "total_results": res.get("totalResults"),
        "current_page": page
    }