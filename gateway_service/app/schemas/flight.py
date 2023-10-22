from pydantic import BaseModel, constr, conint
from datetime import datetime as dt


def convert_datetime_to_iso_8601_without_time_zone(datetime: dt) -> str:
    return datetime.strftime('%Y-%m-%d %H:%M')


class Flight(BaseModel):
    flightNumber: constr(max_length=20)
    fromAirport: str | None
    toAirport: str | None
    date: dt
    price: conint(ge=1)

    class Config:
        json_encoders = {
            # custom output conversion for datetime
            dt: convert_datetime_to_iso_8601_without_time_zone
        }


class FlightList(BaseModel):
    page: conint(ge=0)
    pageSize: conint(ge=1)
    totalElements: conint(ge=0)
    items: list[Flight]
