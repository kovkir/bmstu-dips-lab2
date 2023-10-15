from enum import Enum

from schemas.response import ErrorResponse, ValidationErrorResponse
from schemas.ticket import Ticket

class RespEnum(Enum):
    GetAll = {
        "model": list[Ticket],
        "description": "All Tickets",
    }
    GetByUID = {
        "model": Ticket,
        "description": "Ticket by UID",
    }
    Created = {
        "description": "Created new Ticket",
        "headers": {
            "Location": {
                "description": "Path to new Ticket",
                "style": "simple",
                "schema": {
                    "type": "string"
                }
            }
        },
        "content": {
            "application/octet-stream": {
                "example": ""
            }
        },
    }
    Delete = {
        "description": "Ticket by UID was removed",
        "content": {
            "application/octet-stream": {
                "example": ""
            }
        },
    }
    Patch = {
        "model": Ticket,
        "description": "Ticket by UID was updated",
    }


    InvalidData = {
        "model": ValidationErrorResponse,
        "description": "Invalid data",
    }
    NotFound = {
        "model": ErrorResponse,
        "description": "Not found Ticket by UID",
    }
    Conflict = {
        "model": ErrorResponse,
        "description": "Conflict",
    }

    Health = {
        "description": "Ticket server is ready to work",
        "content": {
            "application/octet-stream": {
                "example": ""
            }
        },
    }
