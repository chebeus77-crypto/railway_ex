import os
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# .env 파일 로드 (프로젝트 루트 기준)
env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=env_path)

# 환경변수 이름은 database_URL (소문자)
DATABASE_URL = os.getenv("database_URL")
if not DATABASE_URL:
    # 로컬 개발용 SQLite 사용
    DATABASE_URL = "sqlite:///./sqlite.db"

# SQLite 전용 설정 (check_same_thread=False)
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
