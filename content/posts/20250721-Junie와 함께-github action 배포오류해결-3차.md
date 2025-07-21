---
title: "Junie와 함께-github action 배포오류해결-3차"
date: 2025-07-21T18:08:00+09:00
draft: false
tags: 
  - junie
  - AI
  - webstorm
  - jetbrain
  - hugo
categories:
  - dev
  - junie
layout: post
---
# GitHub Pages 배포 문제 트러블슈팅

## 문제 설명
GitHub Pages 배포가 다음과 같은 오류로 실패하고 있습니다:
```
Getting Pages deployment status...
Current status: updating_pages
Getting Pages deployment status...
Error: Getting Pages deployment status failed
Error: HttpError: Server Error
    at /home/runner/work/_actions/actions/deploy-pages/v4/node_modules/@octokit/request/dist-node/index.js:124:1
    at processTicksAndRejections (node:internal/process/task_queues:95:5)
    at getPagesDeploymentStatus (/home/runner/work/_actions/actions/deploy-pages/v4/src/internal/api-client.js:143:1)
    at Deployment.check (/home/runner/work/_actions/actions/deploy-pages/v4/src/internal/deployment.js:159:1)
    at main (/home/runner/work/_actions/actions/deploy-pages/v4/src/index.js:40:1)
Getting Pages deployment status...
Current status: updating_pages
Getting Pages deployment status...
Current status: updating_pages
```

배포가 "updating_pages" 상태에서 멈춘 후 서버 오류가 발생하고 있습니다.

## 이전 해결책
이전에 다음과 같은 해결책을 구현했습니다:

1. CNAME 파일을 `static` 디렉토리에 복사하여 빌드에 포함되도록 함
2. `.nojekyll` 파일을 `static` 디렉토리에 생성하여 GitHub Pages가 Jekyll로 처리하지 않도록 함
3. GitHub 워크플로우의 Hugo 버전을 0.128.0에서 0.148.1로 업데이트하여 로컬 환경과 일치시킴

## 수행한 트러블슈팅 단계

### 1. 워크플로우 구성 확인
GitHub Actions 워크플로우 파일(`.github/workflows/hugo.yml`)을 검사하여 다음을 확인했습니다:
- 올바른 Hugo 버전(0.148.1) 사용
- GitHub Pages 배포에 필요한 권한 설정
- 적절한 빌드 및 배포 단계 구성

### 2. 빌드 크기 및 파일 제한 확인
- `public` 디렉토리 크기: 1.6MB (GitHub Pages 제한 내)
- 특수 문자나 비정상적인 이름을 가진 파일 없음

### 3. 필수 파일 확인
다음 파일들이 `static` 디렉토리에 존재하고 빌드 후 `public` 디렉토리에 포함되는지 확인했습니다:
- CNAME 파일 (사용자 정의 도메인 설정용)
- .nojekyll 파일 (Jekyll 처리 방지용)

### 4. Hugo 버전 호환성 확인
Hugo 버전 0.148.1에 대해 GitHub Pages와의 알려진 호환성 문제가 있는지 확인했습니다.

### 5. CNAME 파일 내용 확인
CNAME 파일의 내용이 올바르게 포맷되어 있고 후행 공백이나 특수 문자가 없는지 확인했습니다.

### 6. DNS 구성 확인
Hugo 구성의 baseURL(`https://blog.bestf.net/`)이 CNAME 파일의 사용자 정의 도메인(`blog.bestf.net`)과 일치하는지 확인했습니다.

### 7. GitHub Pages 서비스 상태 확인
GitHub Status 페이지에서 GitHub Pages 서비스에 영향을 미치는 진행 중인 문제가 있는지 확인했습니다.

### 8. 간소화된 빌드 테스트
간단한 테스트 페이지(`test.html`)를 생성하여 최소한의 콘텐츠로 빌드가 성공적으로 배포될 수 있는지 테스트했습니다.

## 추가 트러블슈팅 제안

### 1. GitHub Pages 캐시 초기화
GitHub Pages 배포 캐시를 초기화하는 것이 도움이 될 수 있습니다. 이는 저장소 설정에서 GitHub Pages를 비활성화한 후 다시 활성화하여 수행할 수 있습니다.

### 2. 사용자 정의 도메인 일시적으로 비활성화
사용자 정의 도메인 구성이 문제의 원인일 수 있습니다. 일시적으로 사용자 정의 도메인을 비활성화하고 기본 GitHub Pages 도메인(`username.github.io/repo-name`)으로 배포를 시도해 볼 수 있습니다.

### 3. 대체 배포 방법 고려
GitHub Pages 배포가 계속 실패하는 경우, Netlify, Vercel 또는 Cloudflare Pages와 같은 대체 정적 사이트 호스팅 서비스를 고려해 볼 수 있습니다.

### 4. 다른 브랜치에 배포 시도
`main` 브랜치 대신 `gh-pages` 브랜치에 배포를 시도하거나, 새로운 브랜치를 생성하여 배포를 시도해 볼 수 있습니다.

## 결론
현재까지의 트러블슈팅으로는 GitHub Pages 배포 실패의 명확한 원인을 파악하지 못했습니다. 이는 GitHub의 인프라 문제, 레이트 리미팅, 또는 우리가 직접 제어하거나 진단할 수 없는 다른 외부 요인과 관련되어 있을 수 있습니다.

위에서 제안한 추가 트러블슈팅 단계를 시도하고, GitHub 지원팀에 문의하여 더 자세한 정보를 얻는 것이 좋습니다.

## 다음 단계
1. 간소화된 빌드로 테스트 페이지를 GitHub에 푸시하여 배포 시도
2. GitHub Pages 캐시 초기화 시도
3. 사용자 정의 도메인을 일시적으로 비활성화하고 배포 시도
4. 필요한 경우 대체 배포 방법 고려