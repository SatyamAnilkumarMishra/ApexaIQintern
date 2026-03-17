from fastapi import APIRouter
from app.services.geo_service import get_ip_location

router = APIRouter(
    prefix="/geo",
    tags=["Geolocation API"]
)


@router.get("/{ip}")
def geo_lookup(ip: str):
    return get_ip_location(ip)