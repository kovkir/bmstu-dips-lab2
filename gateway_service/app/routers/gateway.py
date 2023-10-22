from fastapi import APIRouter, Depends, status, Query, Header
from fastapi.responses import Response
from typing import Annotated

from schemas.flight import FlightList
from schemas.ticket import Ticket
from services.gateway import GatewayService
from enums.responses import RespEnum
from cruds.interfaces.flight import IFlightCRUD
from cruds.interfaces.ticket import ITicketCRUD
from cruds.flight import FlightCRUD
from cruds.ticket import TicketCRUD


def get_flight_crud() -> type[FlightCRUD]:
    return FlightCRUD

def get_ticket_crud() -> type[TicketCRUD]:
    return TicketCRUD


router = APIRouter(
    tags=["Gateway API"],
    responses={
        status.HTTP_400_BAD_REQUEST: RespEnum.InvalidData.value,
    }
)


@router.get(
    "/flights", 
    status_code=status.HTTP_200_OK,
    response_model=FlightList,
    responses={
        status.HTTP_200_OK: RespEnum.GetAllFlights.value,
    }
)
async def get_list_of_flights(
        flightCRUD: Annotated[IFlightCRUD, Depends(get_flight_crud)],
        ticketCRUD: Annotated[ITicketCRUD, Depends(get_ticket_crud)],
        page: Annotated[int, Query(ge=0)] = 0,
        size: Annotated[int, Query(ge=1)] = 100
    ):
    return await GatewayService(
            flightCRUD=flightCRUD,
            ticketCRUD=ticketCRUD
        ).get_list_of_flights(
            page=page, 
            size=size
        )


@router.get(
    "/tickets", 
    status_code=status.HTTP_200_OK,
    response_model=list[Ticket],
    responses={
        status.HTTP_200_OK: RespEnum.GetAllTickets.value,
    }
)
async def get_information_on_all_user_tickets(
        flightCRUD: Annotated[IFlightCRUD, Depends(get_flight_crud)],
        ticketCRUD: Annotated[ITicketCRUD, Depends(get_ticket_crud)],
        X_User_Name: Annotated[str, Header(max_length=80)],
    ):
    return await GatewayService(
            flightCRUD=flightCRUD,
            ticketCRUD=ticketCRUD
        ).get_info_on_all_user_tickets(
            user_name=X_User_Name
        )
