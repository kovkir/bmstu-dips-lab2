from uuid import UUID

from models.ticket import TicketModel
from schemas.ticket import TicketUpdate
from cruds.interfaces.ticket import ITicketCRUD


class TicketCRUD(ITicketCRUD):
    async def get_all(self, offset: int = 0, limit: int = 100):
        return self._db.query(TicketModel).offset(offset).limit(limit).all()

    async def get_by_uid(self, ticket_uid: UUID):
        return self._db.query(TicketModel).filter(
            TicketModel.ticket_uid == ticket_uid).first()
    
    async def add(self, ticket: TicketModel):
        try:
            self._db.add(ticket)
            self._db.commit()
            self._db.refresh(ticket)
        except:
            return None
        
        return ticket

    async def delete(self, ticket: TicketModel):
        self._db.delete(ticket)
        self._db.commit()
        
        return ticket
    
    async def patch(self, ticket: TicketModel, ticket_update: TicketUpdate):
        update_fields = ticket_update.model_dump(exclude_unset=True)        
        for key, value in update_fields.items():
            setattr(ticket, key, value)
        
        try:
            self._db.add(ticket)
            self._db.commit()
            self._db.refresh(ticket)
        except:
            return None
        
        return ticket
