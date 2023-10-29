from enum import Enum

from schemas.response import ErrorResponse, ValidationErrorResponse
from schemas.flight import PaginationResponse
from schemas.ticket import TicketResponse, TicketPurchaseResponse
from schemas.user import UserInfoResponse


class RespEnum(Enum):
    GetAllFlights = {
        "model": PaginationResponse,
        "description": "Список рейсов",
    }
    GetAllTickets = {
        "model": list[TicketResponse],
        "description": "Информация по всем билетам пользователя",
    }
    GetTicket = {
        "model": TicketResponse,
        "description": "Информация по конкретному билету",
    }
    BuyTicket = {
        "model": TicketPurchaseResponse,
        "description": "Информация о купленном билете",
    }
    TicketRefund = {
        "description": "Возврат билета успешно выполнен",
        "content": {
            "application/octet-stream": {
                "example": ""
            }
        },
    }
    GetMe = {
        "model": UserInfoResponse,
        "description": "Полная информация о пользователе",
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
