from abc import ABC, abstractmethod

from schemas.bonus import PrivilegeHistoryCreate, PrivilegeCreate


class IBonusCRUD(ABC):
    @abstractmethod
    async def get_all_privileges(
            self, 
            page: int = 0, 
            size: int = 100,
            username: str | None = None
        ) -> list[dict]:
        pass
    
    @abstractmethod
    async def get_privilege_by_id(self, privilege_id: int) -> dict:
        pass
    
    @abstractmethod
    async def create_new_privilege(self, privilege_create: PrivilegeCreate) -> int:
        pass

    @abstractmethod
    async def create_new_privilege_history(self, history_create: PrivilegeHistoryCreate) -> int:
        pass
