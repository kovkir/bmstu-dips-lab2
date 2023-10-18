from pydantic import BaseModel
from datetime import datetime as dt
from uuid import UUID

from enums.status import PrivilegeHistoryStatus


class PrivilegeHistoryBase(BaseModel):
    privilege_id: int | None
    ticket_uid: UUID
    balance_diff: int
    operation_type: PrivilegeHistoryStatus


class PrivilegeHistoryFilter(BaseModel):
    privilege_id: int | None


class PrivilegeHistoryCreate(PrivilegeHistoryBase):
    pass


class PrivilegeHistory(PrivilegeHistoryBase):
    id: int
    datetime: dt