import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .database import Base, engine
from .routers import reservation

# DB 테이블 자동 생성
Base.metadata.create_all(bind=engine)

app = FastAPI(title="회의실 예약 시스템")

# 현재 파일 기준 경로
BASE_DIR = os.path.dirname(__file__)

# 템플릿 설정
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# 정적 파일 마운트 (폴더가 있을 때만)
static_dir = os.path.join(BASE_DIR, "static")
if os.path.isdir(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

# 라우터 등록
app.include_router(reservation.router)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """메인 대시보드 페이지"""
    return templates.TemplateResponse("index.html", {"request": request})
