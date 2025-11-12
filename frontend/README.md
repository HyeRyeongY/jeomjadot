# 점자닷 Frontend

Next.js 15 기반 한글 점자 변환 웹 애플리케이션

## 설치

```bash
npm install
```

## 개발 서버 실행

```bash
npm run dev
```

브라우저에서 http://localhost:3000 열기

## 빌드

```bash
npm run build
npm run start
```

## 환경 변수

`.env.local` 파일 생성:

```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

프로덕션 배포 시:

```
NEXT_PUBLIC_API_URL=https://your-backend-api.onrender.com
```

## 배포

### Vercel

```bash
npm run build
vercel --prod
```

또는 GitHub 연동으로 자동 배포

## 기술 스택

- Next.js 15
- React 19
- TypeScript
- Tailwind CSS
- App Router
