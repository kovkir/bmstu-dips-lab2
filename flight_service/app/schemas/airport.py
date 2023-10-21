from pydantic import BaseModel, constr


class AirportBase(BaseModel):
    name: constr(max_length=255) | None = None
    city: constr(max_length=255) | None = None
    country: constr(max_length=255) | None = None


class AirportCreate(AirportBase):
    pass


class Airport(AirportBase):
    id: int
