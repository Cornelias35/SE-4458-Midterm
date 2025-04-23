from fastapi import FastAPI

from app.controller import flight_controller, query_flight_passenger_controller, ticket_controller, auth_controller
from fastapi_pagination import add_pagination
from app.database.session import engine, SessionLocal

from app.models.database_models import Base


app = FastAPI()

app.include_router(flight_controller.router)

app.include_router(query_flight_passenger_controller.router)
app.include_router(ticket_controller.router)

app.include_router(auth_controller.router)

Base.metadata.create_all(bind=engine)

add_pagination(app)

@app.get("/")
async def root():
    return {"message": "Bedirhan Kırtan SE 4458 Midterm Project"}

