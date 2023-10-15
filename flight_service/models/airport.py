from sqlalchemy import Column, Integer, String
from utils.database import Base


class AirportModel(Base):
    __tablename__ = "airports"
    __table_args__ = {'extend_existing': True}
    
    id      = Column(Integer, primary_key=True, index=True)
    name    = Column(String(255))
    city    = Column(String(255))
    country = Column(String(255))
