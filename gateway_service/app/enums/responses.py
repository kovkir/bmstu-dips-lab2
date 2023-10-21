from enum import Enum

from schemas.response import ErrorResponse, ValidationErrorResponse
from schemas.flight import FlightsList


class RespEnum(Enum):
    GetAllFlights = {
        "model": FlightsList,
        "description": "Список рейсов",
    }

    InvalidData = {
        "model": ValidationErrorResponse,
        "description": "Ошибка валидации данных",
    }
    