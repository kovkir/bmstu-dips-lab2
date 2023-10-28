import json
import requests
from requests import Response
from fastapi import status

from utils.settings import get_settings
from cruds.interfaces.bonus import IBonusCRUD
from cruds.base import BaseCRUD
from schemas.bonus import (
    PrivilegeHistoryCreate, 
    PrivilegeCreate, 
    PrivilegeUpdate
)


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
        if response.status_code == status.HTTP_404_NOT_FOUND:
            return None
        else:
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
    
    async def update_privilege_by_id(
            self, 
            privilege_id: int,
            privilege_update: PrivilegeUpdate
        ):
        response: Response = requests.patch(
            url=f'{self.http_path}privileges/{privilege_id}/',
            data=json.dumps(privilege_update.model_dump(exclude_unset=True))
        )
        self._check_status_code(response.status_code)

        return response.json()
    
    async def create_new_privilege_history(
            self, 
            privilege_history_create: PrivilegeHistoryCreate
        ):
        response: Response = requests.post(
            url=f'{self.http_path}privilege_histories/',
            data=json.dumps(privilege_history_create.model_dump(exclude_unset=True))
        )
        self._check_status_code(response.status_code)
        
        location: str = response.headers["location"]
        id_ = int(location.split("/")[-1])

        return id_
    