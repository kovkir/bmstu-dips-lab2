from pydantic import BaseModel, constr, conint
from datetime import datetime as dt


class Flight(BaseModel):
    flightNumber: constr(max_length=20)
    price: conint(ge=1)
    datetime: dt
    fromAirport: str | None = None
    toAirport: str | None = None


class FlightsList(BaseModel):
    page: conint(ge=0)
    pageSize: conint(ge=1)
    totalElements: conint(ge=0)
    items: list[Flight]
