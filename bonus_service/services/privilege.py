from sqlalchemy.orm import Session

from models.privilege import PrivilegeModel
from schemas.privilege import PrivilegeCreate, PrivilegeUpdate
from exceptions.http_exceptions import NotFoundException, ConflictException
from cruds.interfaces.privilege import IPrivilegeCRUD


class PrivilegeService():
    def __init__(self, privilegeCRUD: type[IPrivilegeCRUD], db: Session):
        self._privilegeCRUD = privilegeCRUD(db)
        
    async def get_all(
            self,
            page: int = 0,
            size: int = 100
        ):
        return await self._privilegeCRUD.get_all(
                offset=page * size, 
                limit=size
            )

    async def get_by_id(self, privilege_id: int):
        privilege = await self._privilegeCRUD.get_by_id(privilege_id)
        if privilege == None:
            raise NotFoundException(
                prefix="Get Privilege",
                search_field="id"
            )
        
        return privilege
    
    async def get_by_username(self, username: str):
        privilege = await self._privilegeCRUD.get_by_username(username)
        if privilege == None:
            raise NotFoundException(
                prefix="Get Privilege",
                search_field="username"
            )
        
        return privilege
    
    async def add(self, privilege_create: PrivilegeCreate):
        privilege = PrivilegeModel(**privilege_create.model_dump())
        privilege = await self._privilegeCRUD.add(privilege)
        if privilege == None:
            raise ConflictException(prefix="Add Privilege")
        
        return privilege
    
    async def delete(self, privilege_id: int):
        privilege = await self._privilegeCRUD.get_by_id(privilege_id)
        if privilege == None:
            raise NotFoundException(
                prefix="Delete Privilege",
                search_field="id"
            )
        
        return await self._privilegeCRUD.delete(privilege)

    async def patch(self, privilege_id: int, privilege_update: PrivilegeUpdate):
        privilege = await self._privilegeCRUD.get_by_id(privilege_id)
        if privilege == None:
            raise NotFoundException(
                prefix="Update Privilege",
                search_field="id"
            )
    
        privilege = await self._privilegeCRUD.patch(privilege, privilege_update)
        if privilege == None:
            raise ConflictException(prefix="Update Privilege")
        
        return privilege
