from fastapi import APIRouter
from app.services.news_service import getTopHeadlines

router=APIRouter(prefix="/news",tags=["News API"])

@router.get("/")
def fetchMovies(country: str = "us", category: str = None, page: int = 1):
    return getTopHeadlines(country,category,page)