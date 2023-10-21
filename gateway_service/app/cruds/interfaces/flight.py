from abc import ABC, abstractmethod
from requests import Response


class IFlightCRUD(ABC):
    @abstractmethod
    async def get_all_flights(self, page: int, size: int) -> Response:
       pass
    
    @abstractmethod
    async def get_airport_by_id(self, airport_id: int) -> Response:
        pass
