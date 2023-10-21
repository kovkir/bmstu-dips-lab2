from pydantic import BaseModel, constr, conint
from datetime import datetime as dt


class Flights(BaseModel):
    flight_number: constr(max_length=20)
    price: conint(ge=1)
    datetime: dt
    from_airport_id: conint(ge=1) | None = None
    to_airport_id: conint(ge=1) | None = None

class FlightsList(BaseModel):
    page: conint(ge=0)
    pageSize: conint(ge=1)
    totalElements: conint(ge=0)
    items: list[Flights]
