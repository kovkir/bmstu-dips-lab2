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
    GetTicket = {
        "model": Ticket,
        "description": "Информация по конкретному билету",
    }
    BuyTicket = {
        "model": TicketPurchaseResponse,
        "description": "Информация о купленном билете",
    }

    FlightNumberNotFound = {
        "model": ErrorResponse,
        "description": "Рейс с таким номером не найден",
    }
    TicketNotFound = {
        "model": ErrorResponse,
        "description": "Билет не найден",
    }
    InvalidData = {
        "model": ValidationErrorResponse,
        "description": "Ошибка валидации данных",
    }
