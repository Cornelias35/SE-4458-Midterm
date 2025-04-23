from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.database.session import Base

class FlightDB(Base):
    __tablename__ = "flights"
    id = Column(Integer, primary_key=True, index=True)
    date_from = Column(DateTime)
    date_to = Column(DateTime)
    airport_from = Column(String)
    airport_to = Column(String)
    duration = Column(Integer)
    capacity = Column(Integer)
    one_way = Column(Boolean)

class TicketDB(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, index=True)
    flight_number = Column(Integer)
    date = Column(DateTime)
    passenger_name = Column(String)

class UserDB(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
