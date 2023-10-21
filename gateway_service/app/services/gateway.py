from requests import Response
from json import loads

from schemas.flight import FlightsList, Flight
from exceptions.http_exceptions import NotFoundException, ConflictException
from cruds.interfaces.flight import IFlightCRUD


class GatewayService():
    def __init__(
            self, 
            flightCRUD: type[IFlightCRUD]
        ):
        self._flightCRUD = flightCRUD()
        
    async def get_list_of_flights(self, page: int, size: int):
        response: Response = await self._flightCRUD.get_all_flights(page, size)
        flights_list = response.json()

        items = []
        for flight_dict in flights_list:
            fromAirport = await self.__get_airport_by_id(flight_dict["from_airport_id"])
            toAirport = await self.__get_airport_by_id(flight_dict["to_airport_id"])

            items.append(
                Flight(
                    flightNumber=flight_dict["flight_number"],
                    price=flight_dict["price"],
                    datetime=flight_dict["datetime"],
                    fromAirport=fromAirport,
                    toAirport=toAirport
                )
            )

        return FlightsList(
                page=page,
                pageSize=size,
                totalElements=len(items),
                items=items
            )
    
    async def __get_airport_by_id(self, airport_id: int):
        if airport_id:
            response: Response = await self._flightCRUD.get_airport_by_id(airport_id)
            airport_dict = response.json()

            airport = f"{airport_dict['city']} {airport_dict['name']}"
        else:
            airport = None

        return airport
