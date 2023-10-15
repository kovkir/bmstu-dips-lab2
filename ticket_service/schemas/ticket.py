from pydantic import BaseModel, ConfigDict, constr, conint
from uuid import UUID

from enums.status import TicketStatus


class TicketBase(BaseModel):
    username: constr(max_length=80)
    flight_number: constr(max_length=20)
    price: conint(ge=1)
    status: TicketStatus


class TicketUpdate(BaseModel):
    status: TicketStatus


class TicketCreate(TicketBase):
    pass


class Ticket(TicketBase):
    id: int
    ticket_uid: UUID
