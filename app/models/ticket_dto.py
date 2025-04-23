from pydantic import BaseModel
from datetime import datetime

class TicketDTO(BaseModel):
    flight_number : int
    date: datetime
    passenger_name: str
