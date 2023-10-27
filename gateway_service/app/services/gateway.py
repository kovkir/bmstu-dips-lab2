from cruds.interfaces.flight import IFlightCRUD
from cruds.interfaces.ticket import ITicketCRUD
from cruds.interfaces.bonus import IBonusCRUD
from exceptions.http_exceptions import NotFoundException
from enums.status import TicketStatus
from schemas.flight import (
    FlightList, 
    Flight
)
from schemas.bonus import (
    PrivilegeShortInfo, 
    PrivilegeCreate, 
    PrivilegeHistoryCreate
)
from schemas.ticket import (
    Ticket,
    TicketCreate, 
    TicketPurchaseRequest, 
    TicketPurchaseResponse
)


class GatewayService():
    def __init__(
            self, 
            flightCRUD: type[IFlightCRUD],
            ticketCRUD: type[ITicketCRUD],
            bonusCRUD:  type[IBonusCRUD]
        ):
        self._flightCRUD = flightCRUD()
        self._ticketCRUD = ticketCRUD()
        self._bonusCRUD  = bonusCRUD()
        
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
    
    async def buy_ticket(
            self, 
            user_name: str,
            ticket_purchase_request: TicketPurchaseRequest
        ):
        flight_dict = await self.__get_flight_by_number(ticket_purchase_request.flightNumber)
        if  flight_dict == None:
            raise NotFoundException(
                prefix="Buy Ticket",
                message="Рейса с таким номером не существует"
            )
        
        paid_by_bonuses, paid_by_money, privilege = await self.__paid_ticket(
            user_name=user_name,
            price=ticket_purchase_request.price,
            paid_from_balance=ticket_purchase_request.paidFromBalance
        )

        ticket_dict = await self.__get_new_ticket(
            username=user_name,
            flight_number=ticket_purchase_request.flightNumber,
            price=paid_by_money
        )

        return TicketPurchaseResponse(
                ticketUid=ticket_dict["ticket_uid"],
                fromAirport=await self.__get_airport_by_id(flight_dict["from_airport_id"]),
                toAirport=await self.__get_airport_by_id(flight_dict["to_airport_id"]),
                date=flight_dict["datetime"],
                price=ticket_purchase_request.price,
                paidByMoney=paid_by_money,
                paidByBonuses=paid_by_bonuses,
                status=ticket_dict["status"],
                privilege=privilege
            )
        
    async def __paid_ticket(
            self, 
            user_name: str, 
            price: int, 
            paid_from_balance: bool
        ):
        privilege_dict = await self.__get_privilege_by_username(user_name)
        if privilege_dict == None:
            privilege_dict = await self.__get_new_privilege(user_name)
        
        if paid_from_balance:
            paid_by_bonuses = min(price, privilege_dict["balance"])
            paid_by_money = price - paid_by_bonuses
            privilege = PrivilegeShortInfo(
                balance=privilege_dict["balance"] - paid_by_bonuses,
                status=privilege_dict["status"]
            )

            # await self.__add_bonuses()
        else:
            paid_by_bonuses = 0
            paid_by_money = price
            privilege = PrivilegeShortInfo(
                balance=privilege_dict["balance"] - paid_by_bonuses,
                status=privilege_dict["status"]
            )

            # await self.__write_off_bonuses()

        return paid_by_bonuses, paid_by_money, privilege

    # async def __write_off_bonuses(self):
    #     pass

    # async def __add_bonuses(self):
    #     pass

    async def __get_new_privilege(self, username: str):
        privilege_id = await self._bonusCRUD.create_new_privilege(
            PrivilegeCreate(
                username=username,
                balance=0
            )
        )
        privilege_dict = await self._bonusCRUD.get_privilege_by_id(privilege_id)

        return privilege_dict
    
    async def __get_new_ticket(self, username: str, flight_number: str, price: str):
        ticket_uid = await self._ticketCRUD.create_new_ticket(
            TicketCreate(
                username=username,
                flight_number=flight_number,
                price=price,
                status=TicketStatus.Paid.value
            )
        )
        ticket_dict = await self._ticketCRUD.get_ticket_by_uid(ticket_uid)

        return ticket_dict
        
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
        flight_dict = flight_list[0] if len(flight_list) else None

        return flight_dict
    
    async def __get_privilege_by_username(self, username: str):
        privilege_list = await self._bonusCRUD.get_all_privileges(
            username=username
        )
        privilege_dict = privilege_list[0] if len(privilege_list) else None

        return privilege_dict
