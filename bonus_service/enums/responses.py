from enum import Enum

from schemas.response import ErrorResponse, ValidationErrorResponse
from schemas.privilege_history import PrivilegeHistory
from schemas.privilege import Privilege


class RespPrivilegeEnum(Enum):
    GetAll = {
        "model": list[Privilege],
        "description": "All Privileges",
    }
    GetByID = {
        "model": Privilege,
        "description": "Privilege by ID",
    }
    Created = {
        "description": "Created new Privilege",
        "headers": {
            "Location": {
                "description": "Path to new Privilege",
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
        "description": "Privilege by ID was removed",
        "content": {
            "application/octet-stream": {
                "example": ""
            }
        },
    }
    Patch = {
        "model": Privilege,
        "description": "Privilege by ID was updated",
    }


    InvalidData = {
        "model": ValidationErrorResponse,
        "description": "Invalid data",
    }
    NotFound = {
        "model": ErrorResponse,
        "description": "Not found Privilege by ID",
    }
    Conflict = {
        "model": ErrorResponse,
        "description": "Conflict",
    }


class RespPrivilegeHistoryEnum(Enum):
    GetAll = {
        "model": list[PrivilegeHistory],
        "description": "All Privilege Histories",
    }
    GetByID = {
        "model": PrivilegeHistory,
        "description": "Privilege History by ID",
    }
    Created = {
        "description": "Created new Privilege History",
        "headers": {
            "Location": {
                "description": "Path to new Privilege History",
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
        "description": "Privilege History by ID was removed",
        "content": {
            "application/octet-stream": {
                "example": ""
            }
        },
    }
    Patch = {
        "model": PrivilegeHistory,
        "description": "Privilege History by ID was updated",
    }


    InvalidData = {
        "model": ValidationErrorResponse,
        "description": "Invalid data",
    }
    NotFound = {
        "model": ErrorResponse,
        "description": "Not found Privilege History by ID",
    }
    Conflict = {
        "model": ErrorResponse,
        "description": "Conflict",
    }


class RespManageEnum(Enum):
    Health = {
        "description": "Bonus server is ready to work",
        "content": {
            "application/octet-stream": {
                "example": ""
            }
        },
    }
