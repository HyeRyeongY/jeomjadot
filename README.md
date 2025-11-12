# 점자닷 (Jeomjadot)

한글 텍스트를 점자로 변환하는 웹 애플리케이션입니다.

## 📋 프로젝트 개요

점자닷은 한글 텍스트를 점자로 쉽고 빠르게 변환할 수 있는 무료 웹 서비스입니다.
- **프론트엔드**: Next.js 15 (TypeScript, Tailwind CSS)
- **백엔드**: FastAPI (Python 3.11)
- **변환 방식**: 국립국어원 한글 점자 규정 기반 + libLouis fallback (하이브리드)

## 🎯 주요 기능

### 점자 변환
- ✅ **한글 점자 변환**: 자모 분해 방식으로 정확한 점자 생성
- ✅ **숫자 표기**: 숫자표(⠼) 사용한 올바른 숫자 점자 변환
- ✅ **영문자 표기**: 영어표(⠰) + 대문자표(⠠) 사용한 알파벳 변환
- ✅ **문장 부호**: 마침표, 쉼표, 물음표, 느낌표 등 점자 변환
- ✅ **약자 규칙**: 것, 이, 그, 저, 그래서 등 전부/부분 약자 지원
- ✅ **혼합 텍스트**: 한글+숫자+영문+부호 복합 텍스트 처리

### 기타 기능
- ✅ libLouis 통합 지원 (옵션)
- ✅ 반응형 웹 디자인
- ✅ 클립보드 복사 기능
- ✅ API 상태 모니터링
- ✅ 고급 규칙 ON/OFF 선택 가능

## 🏗️ 프로젝트 구조

```
jeomjadot/
├── frontend/          # Next.js 프론트엔드
│   ├── app/
│   │   ├── components/
│   │   ├── lib/
│   │   ├── layout.tsx
│   │   └── page.tsx
│   ├── package.json
│   └── vercel.json
├── backend/           # FastAPI 백엔드
│   ├── app/
│   │   ├── routers/
│   │   ├── services/
│   │   ├── main.py
│   │   └── models.py
│   ├── requirements.txt
│   ├── render.yaml
│   └── Procfile
├── data/              # 샘플 데이터
└── README.md
```

## 🚀 시작하기

### 사전 요구 사항

- Node.js 18+
- Python 3.11+
- npm 또는 yarn

### 백엔드 설치 및 실행

```bash
# 백엔드 디렉토리로 이동
cd backend

# 가상 환경 생성 (권장)
python -m venv venv

# 가상 환경 활성화
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 의존성 설치
pip install -r requirements.txt

# 서버 실행
uvicorn app.main:app --reload --port 8000
```

백엔드 서버가 http://localhost:8000 에서 실행됩니다.
- API 문서: http://localhost:8000/docs
- 상태 확인: http://localhost:8000/health

### 프론트엔드 설치 및 실행

```bash
# 프론트엔드 디렉토리로 이동
cd frontend

# 의존성 설치
npm install

# 환경 변수 설정
# .env.local 파일 생성 (이미 생성됨)
# NEXT_PUBLIC_API_URL=http://localhost:8000

# 개발 서버 실행
npm run dev
```

프론트엔드가 http://localhost:3000 에서 실행됩니다.

## 🧪 테스트

### 백엔드 테스트

```bash
cd backend
python test_converter.py
```

### 샘플 데이터

`data/sample_data.csv`와 `data/test_cases.txt`에 테스트용 샘플 데이터가 준비되어 있습니다.

## 📦 배포

### Vercel (프론트엔드)

1. GitHub에 코드 푸시
2. Vercel에서 `frontend` 디렉토리 선택
3. 환경 변수 설정:
   - `NEXT_PUBLIC_API_URL`: 백엔드 API URL

```bash
cd frontend
npm run build
vercel --prod
```

### Render / Railway (백엔드)

#### Render 배포

1. Render 대시보드에서 "New Web Service" 선택
2. GitHub 저장소 연결
3. Root Directory: `backend`
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

또는 `render.yaml` 파일 사용:

```bash
cd backend
# render.yaml 파일이 프로젝트에 포함되어 있음
```

#### Railway 배포

1. Railway 대시보드에서 "New Project" 선택
2. GitHub 저장소 연결
3. Root Directory: `backend`
4. Railway가 자동으로 `Procfile` 감지

## 📚 API 문서

### POST `/api/translate`

한글 텍스트를 점자로 변환합니다.

**요청 본문:**
```json
{
  "text": "안녕하세요",
  "use_liblouis": false
}
```

**응답:**
```json
{
  "original_text": "안녕하세요",
  "braille": "⠣⠒⠜⠶⠚⠣⠎⠥",
  "method": "rule-based",
  "success": true,
  "error": null
}
```

### GET `/api/translate/health`

변환 서비스 상태를 확인합니다.

**응답:**
```json
{
  "status": "healthy",
  "liblouis_available": false
}
```

## 🔧 한글 점자 변환 방식

### Rule-based 방식 (기본)

1. 한글 음절을 초성, 중성, 종성으로 분해
2. 각 자모를 점자로 매핑
3. 유니코드 점자 문자 생성 (U+2800 ~ U+28FF)

**예시:**
- '한' = 'ㅎ' (초성) + 'ㅏ' (중성) + 'ㄴ' (종성)
- '한' → '⠚⠣⠒'

### libLouis 방식 (옵션)

libLouis 라이브러리를 사용한 점자 변환 (설치 필요):

```bash
pip install liblouis
```

## 🛣️ 로드맵

- [ ] 점자 → 한글 역변환 기능
- [ ] 점자 약자 규칙 추가
- [ ] 숫자 및 영어 점자 지원 강화
- [ ] AI 모델 통합 (T5-small fine-tuned)
- [ ] 음성 TTS 기능
- [ ] Haptic 피드백 지원
- [ ] 모바일 앱 개발

## 📄 라이선스

MIT License

## 🤝 기여

기여를 환영합니다! 이슈를 등록하거나 Pull Request를 보내주세요.

## 📞 문의

문의 사항이 있으시면 GitHub Issues를 통해 연락해주세요.

---

**점자닷** - 한글 점자 변환을 더 쉽게
