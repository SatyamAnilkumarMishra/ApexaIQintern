from cachetools import TTLCache

# cache store
weather_cache = TTLCache(maxsize=100, ttl=600)
news_cache = TTLCache(maxsize=100, ttl=600)
currency_cache = TTLCache(maxsize=100, ttl=3600)
holiday_cache = TTLCache(maxsize=100, ttl=86400) 
crypto_cache = TTLCache(maxsize=100, ttl=60)
quote_cache = TTLCache(maxsize=10, ttl=43200)
geo_cache = TTLCache(maxsize=200, ttl=3600)