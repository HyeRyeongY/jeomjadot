# 점자닷 배포 가이드

## 배포 구조

- **프론트엔드** → Vercel (무료)
- **백엔드** → Render 또는 Railway (무료)

---

## 1. Git 저장소 준비

```bash
# Git 초기화
git init

# 모든 파일 추가
git add .

# 첫 커밋
git commit -m "Initial commit: 점자닷 프로젝트"

# GitHub 저장소 생성 후 연결
# https://github.com/new 에서 새 저장소 생성
git remote add origin https://github.com/your-username/jeomjadot.git
git branch -M main
git push -u origin main
```

---

## 2. 백엔드 배포 (Render)

### 2-1. Render 가입 및 설정

1. **Render 계정 생성**
   - https://render.com 접속
   - GitHub 계정으로 Sign Up

2. **New Web Service 생성**
   - Dashboard → **New +** → **Web Service**
   - GitHub 저장소 연결 (jeomjadot)

3. **서비스 설정**
   ```
   Name:           jeomjadot-api
   Region:         Singapore (또는 가장 가까운 지역)
   Branch:         main
   Root Directory: backend
   Runtime:        Python 3
   Build Command:  pip install -r requirements.txt
   Start Command:  uvicorn app.main:app --host 0.0.0.0 --port $PORT
   Instance Type:  Free
   ```

4. **환경 변수** (현재는 필요 없음)

5. **Create Web Service** 클릭

6. **배포 완료 대기** (5-10분)

7. **URL 복사**
   - 예: `https://jeomjadot-api.onrender.com`
   - 이 URL을 메모장에 저장해두세요!

### 2-2. 백엔드 테스트

배포 완료 후:
```
https://jeomjadot-api.onrender.com/health
→ {"status":"healthy"}

https://jeomjadot-api.onrender.com/docs
→ API 문서 확인
```

---

## 3. 프론트엔드 배포 (Vercel)

### 3-1. Vercel 배포 (웹 UI 사용)

1. **Vercel 계정 생성**
   - https://vercel.com 접속
   - GitHub 계정으로 Sign Up

2. **New Project 생성**
   - Dashboard → **Add New** → **Project**
   - GitHub 저장소 Import (jeomjadot)

3. **프로젝트 설정**
   ```
   Framework Preset:  Next.js (자동 감지)
   Root Directory:    frontend
   Build Command:     npm run build
   Output Directory:  .next
   Install Command:   npm install
   ```

4. **환경 변수 추가** ⚠️ 중요!

   **Environment Variables** 섹션에서:
   ```
   Name:  NEXT_PUBLIC_API_URL
   Value: https://jeomjadot-api.onrender.com
   ```
   (2단계에서 복사한 백엔드 URL)

5. **Deploy** 클릭

6. **배포 완료!**
   - 자동 생성 URL: `https://jeomjadot-xxx.vercel.app`
   - 또는 커스텀 도메인 설정 가능

### 3-2. Vercel CLI로 배포 (선택사항)

```bash
# Vercel CLI 설치
npm i -g vercel

# 프론트엔드 디렉토리로 이동
cd frontend

# Vercel 로그인
vercel login

# 배포 테스트
vercel

# 프로덕션 배포
vercel --prod
```

---

## 4. CORS 설정 업데이트

배포 후 Vercel URL을 백엔드 CORS 설정에 추가:

`backend/app/main.py` 파일 수정:

```python
allow_origins=[
    "http://localhost:3000",
    "https://*.vercel.app",
    "https://jeomjadot-xxx.vercel.app",  # 실제 Vercel URL로 교체
],
```

수정 후:
```bash
git add .
git commit -m "Update CORS settings for production"
git push
```

Render가 자동으로 재배포합니다.

---

## 5. 배포 확인

### 백엔드 확인
```
https://jeomjadot-api.onrender.com/health
→ {"status": "healthy"}
```

### 프론트엔드 확인
```
https://jeomjadot-xxx.vercel.app
→ 웹사이트 접속 확인
→ 텍스트 입력 후 변환 테스트
```

---

## 6. 자동 배포 설정

### GitHub Push 시 자동 배포

- **Vercel**: main 브랜치 push 시 자동 배포
- **Render**: main 브랜치 push 시 자동 배포

```bash
# 코드 수정 후
git add .
git commit -m "Update features"
git push

# 자동으로 재배포됨!
```

---

## 7. 커스텀 도메인 설정 (선택사항)

### Vercel 도메인 설정

1. Vercel Dashboard → 프로젝트 선택
2. **Settings** → **Domains**
3. 도메인 입력 (예: jeomjadot.com)
4. DNS 설정 안내 따라하기

---

## 문제 해결

### 백엔드 API 연결 실패

1. **백엔드 URL 확인**
   ```
   https://jeomjadot-api.onrender.com/health
   ```

2. **환경 변수 확인**
   - Vercel Dashboard → Settings → Environment Variables
   - `NEXT_PUBLIC_API_URL` 값 확인

3. **CORS 설정 확인**
   - `backend/app/main.py`에 Vercel URL 추가 확인

### Render 무료 플랜 제한

- **Cold Start**: 15분 동안 요청이 없으면 슬립 모드
  - 첫 요청 시 50초 정도 소요
  - 해결: 주기적으로 ping (예: UptimeRobot)

- **월 750시간 무료**
  - 하나의 서비스는 충분히 사용 가능

### Vercel 빌드 실패

```bash
# 로컬에서 빌드 테스트
cd frontend
npm run build

# 에러 확인 후 수정
```

---

## 배포 URL 예시

- **프론트엔드**: https://jeomjadot.vercel.app
- **백엔드**: https://jeomjadot-api.onrender.com
- **API 문서**: https://jeomjadot-api.onrender.com/docs

---

## 비용

- ✅ **Vercel**: 무료 (Hobby 플랜)
- ✅ **Render**: 무료 (Free 플랜)
- ✅ **총 비용**: $0 / 월

---

## 다음 단계

1. ✅ GitHub에 코드 Push
2. ✅ Render에 백엔드 배포
3. ✅ Vercel에 프론트엔드 배포
4. ✅ 환경 변수 설정
5. ✅ 배포 확인 및 테스트
6. 🎉 완료!
