from fastapi import APIRouter, Depends
from datetime import datetime
from app.models import ticket_dto
from app.services.ticket_service import TicketService
from app.dependencies.auth import get_current_user
router = APIRouter(
    prefix="/v1/tickets",
    tags=["tickets"]
)

@router.post("/buy_ticket")
async def add_ticket(
        ticket_dto : ticket_dto.TicketDTO,
        user: dict = Depends(get_current_user)
):

    ticket_service = TicketService()
    status = ticket_service.buy_ticket(ticket_dto)

    return {"message": status}

@router.get("/check_in")
async def check_in(
        ticket_dto : ticket_dto.TicketDTO,
):
    ticket_service = TicketService()
    status = ticket_service.check_in(ticket_dto)
    return {"message": status}