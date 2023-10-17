from sqlalchemy.orm import Session
from abc import ABC, abstractmethod

from models.privilege import PrivilegeModel
from schemas.privilege import PrivilegeUpdate


class IPrivilegeCRUD(ABC):
    def __init__(self, db: Session):
        self._db = db

    @abstractmethod
    async def get_all(
            self,
            offset: int = 0,
            limit: int = 100
        ) -> list[PrivilegeModel]:
       pass
    
    @abstractmethod
    async def get_by_id(self, privilege_id: int) -> PrivilegeModel | None:
        pass

    @abstractmethod
    async def get_by_username(self, username: str) -> PrivilegeModel | None:
        pass

    @abstractmethod
    async def add(self, privilege: PrivilegeModel) -> PrivilegeModel | None:
        pass
    
    @abstractmethod
    async def delete(self, privilege: PrivilegeModel) -> PrivilegeModel:
        pass

    @abstractmethod
    async def patch(
            self, 
            privilege: PrivilegeModel, 
            privilege_update: PrivilegeUpdate
        ) -> PrivilegeModel | None:
        pass
