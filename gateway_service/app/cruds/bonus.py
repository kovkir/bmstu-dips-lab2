import json
import requests
from requests import Response

from utils.settings import get_settings
from cruds.interfaces.bonus import IBonusCRUD
from cruds.base import BaseCRUD
from schemas.bonus import PrivilegeHistoryCreate, PrivilegeCreate


class BonusCRUD(IBonusCRUD, BaseCRUD):
    def __init__(self):
        settings = get_settings()
        bonus_host = settings["services"]["gateway"]["bonus_host"]
        bonus_port = settings["services"]["bonus"]["port"]

        self.http_path = f'http://{bonus_host}:{bonus_port}/api/v1/'

    async def get_all_privileges(
            self,  
            page: int = 0, 
            size: int = 100,
            username: str | None = None
        ):
        response: Response = requests.get(
            url=f'{self.http_path}privileges/?page={page}&size={size}'\
                f'{f"&username={username}" if username else ""}'
        )
        self._check_status_code(response.status_code)
        
        return response.json()
    
    async def get_privilege_by_id(self, privilege_id: int):
        response: Response = requests.get(
            url=f'{self.http_path}privileges/{privilege_id}/'
        )
        self._check_status_code(response.status_code)

        return response.json()
    
    async def create_new_privilege(self, privilege_create: PrivilegeCreate):
        response: Response = requests.post(
            url=f'{self.http_path}privileges/',
            data=json.dumps(privilege_create.model_dump())
        )
        self._check_status_code(response.status_code)
        
        location: str = response.headers["location"]
        id_ = int(location.split("/")[-1])

        return id_
    
    async def create_new_privilege_history(self, history_create: PrivilegeHistoryCreate):
        response: Response = requests.post(
            url=f'{self.http_path}privilege_histories/',
            data=json.dumps(history_create.model_dump())
        )
        self._check_status_code(response.status_code)
        
        location: str = response.headers["location"]
        id_ = int(location.split("/")[-1])

        return id_
    