from requests import Response

from schemas.flight import FlightsList
from exceptions.http_exceptions import NotFoundException, ConflictException
from cruds.interfaces.flight import IFlightCRUD


class GatewayService():
    def __init__(
            self, 
            flightCRUD: type[IFlightCRUD]
        ):
        self._flightCRUD = flightCRUD()
        
    async def get_list_of_flights(self, page: int, size: int):
        flights: Response = await self._flightCRUD.get_all_flights(page, size)
        
        return FlightsList(
                page=page,
                pageSize=size,
                totalElements=len(flights.json()),
                items=flights.json()
            )
