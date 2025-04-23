from datetime import datetime
from typing import List

from fastapi import Depends
from pydantic import BaseModel

from app.models.database_models import FlightDB
from app.models.flight_dto import FlightDTO
from fastapi_pagination import Page, paginate, Params
from app.database.session import engine, SessionLocal


class FlightService:
    def add_flight(self, flight_dto: FlightDTO):
        db_session = SessionLocal()
        print(flight_dto)
        try:
            flight = FlightDB(**flight_dto.dict())
            db_session.add(flight)
            db_session.commit()
            return "success"
        except Exception as e:
            print(e)
            db_session.rollback()
            return "failed"
        finally:
            db_session.close()


    def query_flights(
            self,
            date_from: datetime,
            date_to: datetime,
            airport_from: str,
            airport_to: str,
            number_of_people : int,
            one_way: bool,
            page: int,
            size: int
    ):
        db = SessionLocal()
        offset = (page - 1) * size

        try:
            query = db.query(FlightDB).filter(
                FlightDB.date_from >= date_from,
                FlightDB.date_to <= date_to,
                FlightDB.airport_from == airport_from,
                FlightDB.airport_to == airport_to,
                FlightDB.capacity >= number_of_people,
                FlightDB.one_way == one_way
            ).offset(offset).limit(size)

            flights = query.all()

            return [
                {
                    "id": f.id,
                    "date_from": f.date_from,
                    "date_to": f.date_to,
                    "airport_from": f.airport_from,
                    "airport_to": f.airport_to,
                    "duration": f.duration,
                    "capacity": f.capacity,
                    "one_way": f.one_way
                } for f in flights
            ]

        except Exception as e:
            print(e)
            return []

