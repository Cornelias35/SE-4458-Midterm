from pydantic import BaseModel


class Passenger(BaseModel):
    passenger_name: str
    flight_number: int