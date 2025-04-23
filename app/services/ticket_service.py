import random

from fastapi import HTTPException

from app.database.session import SessionLocal
from app.models.database_models import FlightDB, TicketDB
from app.models.ticket_dto import TicketDTO

class TicketService:
    def buy_ticket(self, ticket: TicketDTO):
        db = SessionLocal()

        flight = db.query(FlightDB).filter(
            FlightDB.id == ticket.flight_number,
            FlightDB.date_from <= ticket.date,
            FlightDB.date_to >= ticket.date
        ).first()

        if not flight:
            raise HTTPException(status_code=404, detail="Flight not found")

        if flight.capacity <= 0:
            return {"transaction_status": "Sold out"}
        flight.capacity -= 1

        new_ticket = TicketDB(
            flight_number=ticket.flight_number,
            passenger_name=ticket.passenger_name,
            date=ticket.date,
        )
        db.add(new_ticket)
        db.commit()
        db.refresh(new_ticket)

        return {
            "transaction_status": "Success",
            "ticket_number": new_ticket.id,
            "flight_number": ticket.flight_number,
            "date": ticket.date,
            "passenger_name": ticket.passenger_name
        }

    def check_in(self, ticket: TicketDTO):
        db = SessionLocal()
        ticket_db = db.query(TicketDB).filter(
            TicketDB.passenger_name == ticket.passenger_name
        ).first()

        if not ticket_db:
            raise HTTPException(status_code=404, detail="Ticket not found")

        flight = db.query(FlightDB).filter(FlightDB.id == ticket_db.flight_number).first()

        if not flight:
            raise HTTPException(status_code=404, detail="Flight not found")


        flight_capacity = flight.capacity

        seat = random.randint(1, flight_capacity)
        # Update the ticket with the assigned seat number

        return {
            "status": "Checked in",
            "passenger_name": ticket_db.passenger_name,
            "flight_number": ticket_db.flight_number,
            "seat_number": seat,
            "date": ticket_db.date
        }

