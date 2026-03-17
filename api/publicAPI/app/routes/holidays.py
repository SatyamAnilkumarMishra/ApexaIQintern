from fastapi import APIRouter
from app.services.holiday_service import getHolidays
from datetime import datetime

router=APIRouter(prefix="/holidays",tags=["Holiday API"])

@router.get("/{country}")
def fetch_Holidays(country:str,year:int = None):
    if year is None:
        year = datetime.now().year

    return getHolidays(country,year)