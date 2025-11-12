from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import translate

app = FastAPI(
    title="점자닷 API",
    description="한글 텍스트를 점자로 변환하는 API",
    version="0.1.0"
)

# CORS 설정 (프론트엔드 연동용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://*.vercel.app",
        "https://jeomjadot.vercel.app",  # 실제 배포 URL로 교체
    ],
    allow_origin_regex=r"https://.*\.vercel\.app",  # 모든 Vercel 도메인 허용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(translate.router, prefix="/api", tags=["translate"])


@app.get("/")
async def root():
    return {
        "message": "점자닷 API에 오신 것을 환영합니다",
        "docs": "/docs",
        "version": "0.1.0"
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
