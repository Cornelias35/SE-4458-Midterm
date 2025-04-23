from fastapi import APIRouter, Depends
from datetime import datetime
from fastapi_pagination import Page, add_pagination
from app.models.Passenger import Passenger
from app.services.get_passenger_service import PassengerService
from app.dependencies.auth import get_current_user

router = APIRouter(
    prefix="/v1/flight-passenger",
    tags=["flight-passenger"]
)
add_pagination(router)


@router.get("/query-flight-passenger-list")
async def query_flight_passenger_list(
        flight_number:int,
        date: datetime,
        page: int = 1,
        size: int = 10,
        user: dict = Depends(get_current_user)

):
    get_flight_passengers = PassengerService()
    passengers = get_flight_passengers.get_passengers(flight_number, date, page, size)
    return {"page": page, "size": size, "passengers": passengers}