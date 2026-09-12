from sqlalchemy import Column, Integer, String, DateTime
from .database import Base

class Reservation(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True, index=True)
    reserver_name = Column(String, nullable=False)
    room_name = Column(String, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
