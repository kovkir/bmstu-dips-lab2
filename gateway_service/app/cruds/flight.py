import requests
from requests import Response

from utils.settings import get_settings


settings = get_settings()


class FlightCRUD():
    async def get_all_flights(self, page: int, size: int) -> Response:
        return requests.get(
                'http://'\
                f'{settings["services"]["gateway"]["flight_host"]}:'\
                f'{settings["services"]["flight"]["port"]}'\
                '/api/v1/flights/'\
                f'?page={page}&size={size}'
            )
    
    async def get_airport_by_id(self, airport_id: int) -> Response:
        return requests.get(
                'http://'\
                f'{settings["services"]["gateway"]["flight_host"]}:'\
                f'{settings["services"]["flight"]["port"]}'\
                '/api/v1/airports/'\
                f'?airport_id={airport_id}'
            )
