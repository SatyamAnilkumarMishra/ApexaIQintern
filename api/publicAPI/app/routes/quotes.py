from fastapi import APIRouter
from app.services.quote_service import getQuote

router=APIRouter(prefix="/quotes",tags=["Quotes API"])

@router.get("/")
def get_quote_of_day():
    return getQuote()