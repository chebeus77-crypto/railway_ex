# ch09_project - Django + Gemini API

Django와 Google Gemini API를 활용한 프로젝트입니다.

## 🛠️ 환경 설정

### 사전 요구사항
- Python 3.12
- [uv](https://docs.astral.sh/uv/) 패키지 매니저

### 설치 및 실행..

```powershell
# 가상환경 생성 및 의존성 설치
uv sync

# Django 개발 서버 실행
uv run python manage.py runserver

# Django 마이그레이션
uv run python manage.py migrate

# 테스트 실행
uv run pytest

# 코드 스타일 검사
uv run ruff check .
uv run ruff format .
```

## 📁 프로젝트 구조

```
ch09_project/
├── .venv/              # uv 가상환경
├── src/
│   └── ch09_project/   # 패키지 소스
├── tests/              # 테스트 코드
├── .env.example        # 환경변수 템플릿
├── .env                # 실제 환경변수 (Git 미포함)
├── .python-version     # Python 3.12 고정
├── pyproject.toml      # 프로젝트 설정
└── README.md
```

## 🔑 환경변수 설정

`.env.example`을 복사하여 `.env` 파일을 생성하고 API 키를 입력하세요:

```powershell
copy .env.example .env
```

| 변수명 | 설명 |
|---|---|
| `DJANGO_SECRET_KEY` | Django 시크릿 키 |
| `DJANGO_DEBUG` | 디버그 모드 여부 |
| `GEMINI_API_KEY` | Google Gemini API 키 |
