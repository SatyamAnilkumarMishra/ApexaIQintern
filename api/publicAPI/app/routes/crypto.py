from fastapi import APIRouter
from app.services.crypto_service import priceTracker

router=APIRouter(prefix="/crypto",tags=["Crypto API"])

@router.get("/")
def price_tracker(coin:str="bitcoin", currency:str="usd"):
    return priceTracker(coin,currency)

