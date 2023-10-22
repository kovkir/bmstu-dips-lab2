import requests
from requests import Response

from utils.settings import get_settings


class TicketCRUD():
    def __init__(self):
        settings = get_settings()
        ticket_host = settings["services"]["gateway"]["ticket_host"]
        ticket_port = settings["services"]["ticket"]["port"]

        self.http_path = f'http://{ticket_host}:{ticket_port}/api/v1/'

    async def get_all_tickets(
            self,
            page: int = 0,
            size: int = 100,
            username: str | None = None
        ):
        response: Response = requests.get(
            url=f'{self.http_path}tickets/?page={page}&size={size}'
                f'{f"&username={username}" if username else ""}'
        )
        return response.json()
    
    async def get_ticket_by_uid(self, ticket_uid: str):
        response: Response = requests.get(
            url=f'{self.http_path}tickets/{ticket_uid}/'
        )
        return response.json()
