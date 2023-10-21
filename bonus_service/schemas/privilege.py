from pydantic import BaseModel, constr

from enums.status import PrivilegeStatus


class PrivilegeBase(BaseModel):
    username: constr(max_length=80)
    status: PrivilegeStatus = 'BRONZE'
    balance: int | None = None


class PrivilegeFilter(BaseModel):
    username: constr(max_length=80) | None = None
    status: PrivilegeStatus | None = None
    

class PrivilegeUpdate(BaseModel):
    status: PrivilegeStatus | None = None
    balance: int | None = None


class PrivilegeCreate(PrivilegeBase):
    pass


class Privilege(PrivilegeBase):
    id: int
