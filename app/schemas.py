from pydantic import BaseModel, Field
from datetime import datetime

class ReservationBase(BaseModel):
    reserver_name: str = Field(..., title="예약자 이름")
    room_name: str = Field(..., title="회의실 이름")
    start_time: datetime = Field(..., title="시작 시간")
    end_time: datetime = Field(..., title="종료 시간")

class ReservationCreate(ReservationBase):
    pass

class ReservationRead(ReservationBase):
    id: int

    class Config:
        from_attributes = True
