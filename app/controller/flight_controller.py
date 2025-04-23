from fastapi import APIRouter, Depends

from app.models.database_models import FlightDB
from app.models.flight_dto import FlightDTO
from datetime import datetime
from app.services.fligth_service import FlightService
from fastapi_pagination import Page, add_pagination, Params, paginate
from app.dependencies.auth import get_current_user
router = APIRouter(
    prefix="/v1/flights",
    tags=["flights"]
)
add_pagination(router)
@router.post("/add_flight")
async def add_flight(
        flight: FlightDTO,
        user: dict = Depends(get_current_user)
):
    flight_service = FlightService()
    status = flight_service.add_flight(flight)

    return {"message": status}

@router.get("/query_flight")
async def query_flight(
        date_from: datetime,
        date_to: datetime,
        airport_from: str,
        airport_to: str,
        number_of_people : int,
        one_way: bool,
        page: int = 1,
        size: int = 10,
):
    flight_service = FlightService()
    flights = flight_service.query_flights(
        date_from=date_from,
        date_to=date_to,
        airport_from=airport_from,
        airport_to=airport_to,
        number_of_people=number_of_people,
        one_way=one_way,
        page=page,
        size=size
    )
    return {
        "page": page,
        "size": size,
        "flights": flights
    }

