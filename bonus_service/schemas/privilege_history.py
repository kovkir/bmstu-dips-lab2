from pydantic import BaseModel
from datetime import datetime as dt
from uuid import UUID

from enums.status import PrivilegeHistoryStatus


class PrivilegeHistoryBase(BaseModel):
    privilege_id: int | None
    ticket_uid: UUID
    datetime: dt
    balance_diff: int
    operation_type: PrivilegeHistoryStatus


class PrivilegeHistoryCreate(PrivilegeHistoryBase):
    pass


class PrivilegeHistory(PrivilegeHistoryBase):
    id: int
