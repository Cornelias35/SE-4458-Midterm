from datetime import datetime
from app.database.session import SessionLocal

from app.models.database_models import FlightDB, TicketDB


class PassengerService:
    def get_passengers(self, flight_number: int, date: datetime, page: int, size: int):
        db = SessionLocal()
        offset = (page - 1) * size

        ticket_db = db.query(TicketDB).filter(
            TicketDB.flight_number == flight_number,
            TicketDB.date == date
        ).offset(offset).limit(size).all()

        return [
            {
                "passenger_name": ticket.passenger_name,
                "date": ticket.date
            } for ticket in ticket_db
        ]

