from enum import Enum

from schemas.response import ErrorResponse, ValidationErrorResponse
from schemas.flight import FlightList
from schemas.ticket import Ticket, TicketPurchaseResponse


class RespEnum(Enum):
    GetAllFlights = {
        "model": FlightList,
        "description": "Список рейсов",
    }
    GetAllTickets = {
        "model": list[Ticket],
        "description": "Информация по всем билетам пользователя",
    }
    BuyTicket = {
        "model": TicketPurchaseResponse,
        "description": "Информация о купленном билете",
    }

    InvalidData = {
        "model": ValidationErrorResponse,
        "description": "Ошибка валидации данных",
    }
