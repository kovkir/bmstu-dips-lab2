from pydantic import BaseModel, conint, constr

from enums.status import PrivilegeHistoryStatus, PrivilegeStatus


class PrivilegeShortInfo(BaseModel):
    balance: conint(ge=0) | None
    status: PrivilegeStatus


class PrivilegeCreate(BaseModel):
    username: constr(max_length=80)
    status: PrivilegeStatus = 'BRONZE'
    balance: conint(ge=0) | None = None


class PrivilegeUpdate(BaseModel):
    status: PrivilegeStatus | None = None
    balance: conint(ge=0) | None = None

class PrivilegeHistoryCreate(BaseModel):
    privilege_id: int | None
    ticket_uid: str
    balance_diff: int
    operation_type: PrivilegeHistoryStatus
