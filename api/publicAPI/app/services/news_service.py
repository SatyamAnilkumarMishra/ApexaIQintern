import requests
from app.config import setting
from app.cache import news_cache

API_KEY=setting.NEWS_API

def getTopHeadlines(country="us",category=None,page=1):
    cache_key = f"{country}-{category}-{page}"
    if cache_key in news_cache:
        return news_cache[cache_key]
    url="https://newsapi.org/v2/top-headlines"

    params={
        "country": country,
        "page": page,
        "pageSize": 10,
        "apiKey": API_KEY
    }
    if category:
        params["category"] = category

    response = requests.get(url, params=params)
    data = response.json()

    articles = []

    for article in data.get("articles", []):
        articles.append({
            "title": article["title"],
            "source": article["source"]["name"],
            "author": article["author"],
            "url": article["url"],
            "published_at": article["publishedAt"]
        })

    result = {
        "totalResults": data.get("totalResults"),
        "page": page,
        "articles": articles
    }
    news_cache[cache_key] = result

    return result