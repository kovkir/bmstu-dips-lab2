from pydantic import BaseModel, constr, conint
from datetime import datetime as dt
from uuid import UUID

from enums.status import TicketStatus
from schemas.bonus import PrivilegeShortInfo


def convert_datetime_to_iso_8601_without_time_zone(datetime: dt) -> str:
    return datetime.strftime('%Y-%m-%d %H:%M')


class Ticket(BaseModel):
    ticketUid: UUID
    flightNumber: constr(max_length=20)
    fromAirport: str | None
    toAirport: str | None
    date: dt
    price: conint(ge=1)
    status: TicketStatus

    class Config:
        json_encoders = {
            # custom output conversion for datetime
            dt: convert_datetime_to_iso_8601_without_time_zone
        }


class TicketPurchaseRequest(BaseModel):
    flightNumber: constr(max_length=20)
    price: conint(ge=1)
    paidFromBalance: bool


class TicketPurchaseResponse(BaseModel):
    ticketUid: UUID
    fromAirport: str | None
    toAirport: str | None
    date: dt
    price: conint(ge=1)
    paidByMoney: conint(ge=0)
    paidByBonuses: conint(ge=0)
    status: TicketStatus
    privilege: PrivilegeShortInfo | None


class TicketCreate(BaseModel):
    username: constr(max_length=80)
    flight_number: constr(max_length=20)
    price: conint(ge=0)
    status: TicketStatus
