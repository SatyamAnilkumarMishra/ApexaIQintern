from fastapi import APIRouter
from app.services.currency_service import currencyConverter

router=APIRouter(prefix="/currency",tags=["Currency API"])

@router.get("/")
def currency_converter(from_currency: str="USD",to_currency: str="INR", amount: float=1.0):
    return currencyConverter(from_currency,to_currency,amount)