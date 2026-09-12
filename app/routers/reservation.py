from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime, time
from .. import schemas, models, database

router = APIRouter(prefix="/api")

@router.get("/reservations", response_model=list[schemas.ReservationRead])
def get_reservations(db: Session = Depends(database.get_db)):
    """오늘(현재 날짜) 기준 9시~18시 예약을 모두 반환한다."""
    today = datetime.now().date()
    start_dt = datetime.combine(today, time(9, 0))
    end_dt = datetime.combine(today, time(18, 0))
    reservations = (
        db.query(models.Reservation)
        .filter(models.Reservation.start_time >= start_dt, models.Reservation.end_time <= end_dt)
        .all()
    )
    return reservations

@router.post("/reserve", status_code=status.HTTP_201_CREATED, response_model=schemas.ReservationRead)
def create_reservation(res: schemas.ReservationCreate, db: Session = Depends(database.get_db)):
    """예약 생성 - 중복(시간 겹침) 방지"""
    # 입력 검증: 종료시간은 시작시간보다 뒤여야 함
    if res.end_time <= res.start_time:
        raise HTTPException(status_code=400, detail="종료시간은 시작시간보다 이후여야 합니다.")
    # 동일 회의실에 겹치는 예약이 있는지 확인
    overlap = (
        db.query(models.Reservation)
        .filter(
            models.Reservation.room_name == res.room_name,
            models.Reservation.start_time < res.end_time,
            models.Reservation.end_time > res.start_time,
        )
        .first()
    )
    if overlap:
        raise HTTPException(status_code=400, detail="이미 예약된 시간과 겹칩니다.")
    db_res = models.Reservation(**res.model_dump())
    db.add(db_res)
    db.commit()
    db.refresh(db_res)
    return db_res
