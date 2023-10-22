from abc import ABC, abstractmethod
from requests import Response


class ITicketCRUD(ABC):
    @abstractmethod
    async def get_all_tickets(
            self, 
            page: int = 0,
            size: int = 100,
            username: str | None = None
        ) -> list[dict]:
       pass

    @abstractmethod
    async def get_ticket_by_uid(self, ticket_uid: str) -> dict:
        pass
