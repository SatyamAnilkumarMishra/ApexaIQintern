from fastapi import APIRouter
from app.services.movie_service import search_Movies

router=APIRouter(prefix="/movies",tags=["Movies API"])

@router.get("/")
def movies(query:str,page:int=1):
    return search_Movies(query,page)