from schemas.flight import FlightList, Flight
from schemas.ticket import Ticket
from cruds.interfaces.flight import IFlightCRUD
from cruds.interfaces.ticket import ITicketCRUD
from exceptions.http_exceptions import NotFoundException, ConflictException


class GatewayService():
    def __init__(
            self, 
            flightCRUD: type[IFlightCRUD],
            ticketCRUD: type[ITicketCRUD]
        ):
        self._flightCRUD = flightCRUD()
        self._ticketCRUD = ticketCRUD()
        
    async def get_list_of_flights(self, page: int, size: int):
        flight_list = await self._flightCRUD.get_all_flights(
            page=page,
            size=size
        )

        flights = []
        for flight_dict in flight_list:
            from_airport = await self.__get_airport_by_id(flight_dict["from_airport_id"])
            to_airport = await self.__get_airport_by_id(flight_dict["to_airport_id"])

            flights.append(
                Flight(
                    flightNumber=flight_dict["flight_number"],
                    fromAirport=from_airport,
                    toAirport=to_airport,
                    date=flight_dict["datetime"],
                    price=flight_dict["price"]
                )
            )

        return FlightList(
                page=page,
                pageSize=size,
                totalElements=len(flights),
                items=flights
            )

    async def get_info_on_all_user_tickets(self, user_name: str):
        ticket_list = await self._ticketCRUD.get_all_tickets(
            username=user_name
        )

        tickets = []
        for ticket_dict in ticket_list:
            flight_dict  = await self.__get_flight_by_number(ticket_dict["flight_number"])
            from_airport = await self.__get_airport_by_id(flight_dict["from_airport_id"])
            to_airport   = await self.__get_airport_by_id(flight_dict["to_airport_id"])

            tickets.append(
                Ticket(
                    ticketUid=ticket_dict["ticket_uid"],
                    flightNumber=ticket_dict["flight_number"],
                    fromAirport=from_airport,
                    toAirport=to_airport,
                    date=flight_dict["datetime"],
                    price=ticket_dict["price"],
                    status=ticket_dict["status"],
                )
            )

        return tickets
        
    async def __get_airport_by_id(self, airport_id: int):
        if airport_id:
            airport_dict = await self._flightCRUD.get_airport_by_id(airport_id)
            airport = f"{airport_dict['city']} {airport_dict['name']}"
        else:
            airport = None

        return airport
    
    async def __get_flight_by_number(self, flight_number: str):
        flight_list = await self._flightCRUD.get_all_flights(
            flight_number=flight_number
        )

        return flight_list[0]
