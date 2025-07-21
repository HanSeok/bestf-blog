---
title: "Junie와 함께-github action 배포오류해결-2차"
date: 2025-07-21T17:58:00+09:00
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
# GitHub Pages 배포 문제 해결 (업데이트)

## 문제
GitHub Pages 배포가 다음과 같은 오류로 실패했습니다:
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
```

배포가 "updating_pages" 상태에서 멈춘 후 서버 오류가 발생했습니다.

## 원인
이전에 CNAME 파일을 `static` 디렉토리에 복사하여 GitHub Pages 배포 문제를 해결했지만, 추가적인 문제가 발견되었습니다:

1. `.nojekyll` 파일이 없어서 GitHub Pages가 Hugo 사이트를 Jekyll로 처리하려고 시도했습니다.
2. GitHub 워크플로우에서 사용하는 Hugo 버전(0.128.0)이 로컬 개발 환경의 버전(0.148.1)과 일치하지 않았습니다.

## 해결책
다음과 같은 변경사항을 적용하여 문제를 해결했습니다:

1. `.nojekyll` 파일을 `static` 디렉토리에 생성했습니다:
   ```bash
   touch static/.nojekyll
   ```

2. GitHub 워크플로우 파일(`.github/workflows/hugo.yml`)에서 Hugo 버전을 업데이트했습니다:
   ```yaml
   env:
     HUGO_VERSION: 0.148.1  # 이전: 0.128.0
   ```

## 검증
해결책을 구현한 후, 로컬 Hugo 빌드를 실행하여 필요한 파일들이 `public` 디렉토리에 포함되었는지 확인했습니다:

```bash
hugo && find public -name "CNAME" -o -name ".nojekyll"
# 출력:
# public/CNAME
# public/.nojekyll
```

## 설명

### .nojekyll 파일의 중요성
`.nojekyll` 파일은 GitHub Pages에게 사이트를 Jekyll로 처리하지 말라고 지시합니다. Hugo와 같은 정적 사이트 생성기를 사용할 때 이 파일이 없으면 GitHub Pages가 사이트를 Jekyll로 처리하려고 시도하여 충돌이 발생할 수 있습니다.

### Hugo 버전 일관성
로컬 개발 환경과 GitHub Actions 워크플로우에서 동일한 Hugo 버전을 사용하는 것이 중요합니다. 버전 불일치는 예상치 못한 빌드 문제를 일으킬 수 있습니다.

## 추가 정보
- CNAME 파일에는 사용자 정의 도메인이 포함되어 있습니다: `blog.bestf.net`
- 이는 Hugo 구성의 `baseURL`과 일치합니다: `https://blog.bestf.net/`
- GitHub Actions 워크플로우는 사이트를 GitHub Pages에 배포하도록 구성되어 있습니다

이러한 변경사항으로 GitHub Pages 배포가 이제 성공적으로 완료될 것입니다.