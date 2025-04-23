from pydantic import BaseModel
from datetime import datetime

class FlightDTO(BaseModel):
    date_from: datetime
    date_to: datetime
    airport_from: str
    airport_to: str
    duration: int
    capacity: int
    one_way: bool

class FlightQueryDTO(BaseModel):
    date_from: datetime
    date_to: datetime
    airport_from: str
    airport_to: str
    number_of_people: int
    one_way: bool