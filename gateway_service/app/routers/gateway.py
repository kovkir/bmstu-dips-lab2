from fastapi import APIRouter, Depends, status, Query
from fastapi.responses import Response
from sqlalchemy.orm import Session
from typing import Annotated

from schemas.flight import FlightsList
from services.gateway import GatewayService
from enums.responses import RespEnum
from cruds.interfaces.flight import IFlightCRUD
from cruds.flight import FlightCRUD


def get_flight_crud() -> type[FlightCRUD]:
    return FlightCRUD


router = APIRouter(
    tags=["Gateway API"],
    responses={
        status.HTTP_400_BAD_REQUEST: RespEnum.InvalidData.value,
    }
)


@router.get(
    "/", 
    status_code=status.HTTP_200_OK,
    response_model=FlightsList,
    responses={
        status.HTTP_200_OK: RespEnum.GetAllFlights.value,
    }
)
async def get_list_of_flights(
        flightCRUD: Annotated[IFlightCRUD, Depends(get_flight_crud)],
        page: Annotated[int, Query(ge=0)] = 0,
        size: Annotated[int, Query(ge=1)] = 100
    ):
    return await GatewayService(
            flightCRUD=flightCRUD,
        ).get_list_of_flights(
            page=page, 
            size=size
        )
