from fastapi import FastAPI
from app.routes import weather, github, movies, news, currency, holidays, crypto, quotes ,geo

app = FastAPI(
    title="Public API Integration Service",
    description="integrating 9 public APIs with caching and error handling",
    version="1.0.0",
)

ENDPOINTS = [
    "/weather",
    "/movies",
    "/github",
    "/news",
    "/currency",
    "/holidays",
    "/crypto",
    "/quotes",
    "/geo",
]
@app.get("/")
async def api_entry_point():
    return {
        "status": "Online",
        "message": "Welcome to the Multi-Service API Hub",
        "total_services": len(ENDPOINTS),
        "endpoints": ENDPOINTS
    }

app.include_router(weather.router)
app.include_router(github.router)
app.include_router(movies.router)
app.include_router(news.router)
app.include_router(currency.router)
app.include_router(holidays.router)
app.include_router(crypto.router)
app.include_router(quotes.router)
app.include_router(geo.router)