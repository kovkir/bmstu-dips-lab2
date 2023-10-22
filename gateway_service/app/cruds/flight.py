import requests
from requests import Response

from utils.settings import get_settings


class FlightCRUD():
    def __init__(self):
        settings = get_settings()
        flight_host = settings["services"]["gateway"]["flight_host"]
        flight_port = settings["services"]["flight"]["port"]

        self.http_path = f'http://{flight_host}:{flight_port}/api/v1/'

    async def get_all_flights(
            self,  
            page: int = 0, 
            size: int = 100,
            flight_number: str | None = None
        ):
        response: Response = requests.get(
            url=f'{self.http_path}flights/?page={page}&size={size}'\
                f'{f"&flight_number={flight_number}" if flight_number else ""}'
        )
        return response.json()
    
    async def get_airport_by_id(self, airport_id: int):
        response: Response = requests.get(
            url=f'{self.http_path}airports/{airport_id}/'
        )
        return response.json()
