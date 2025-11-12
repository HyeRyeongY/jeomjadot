# 점자닷 Backend API

FastAPI 기반 한글 점자 변환 API

## 설치

```bash
# 가상 환경 생성
python -m venv venv

# 가상 환경 활성화 (Windows)
venv\Scripts\activate

# 가상 환경 활성화 (macOS/Linux)
source venv/bin/activate

# 의존성 설치
pip install -r requirements.txt
```

## 실행

```bash
# 개발 서버 실행
uvicorn app.main:app --reload --port 8000

# 프로덕션 서버 실행
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## API 문서

서버 실행 후 다음 URL에서 확인:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 테스트

```bash
python test_converter.py
```

## 배포

### Render

```bash
# render.yaml 파일 사용
```

### Railway

```bash
# Procfile 파일 사용
```

## 환경 변수

필요한 환경 변수는 `.env` 파일에 설정:

```
# 현재 필요한 환경 변수 없음
```
