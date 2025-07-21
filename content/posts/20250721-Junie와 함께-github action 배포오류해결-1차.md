---
title: "Junie와 함께-github action 배포오류해결-1차"
date: 2025-07-21T17:48:00+09:00
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
# GitHub Pages 배포 문제 해결

## 문제
GitHub Pages 배포가 다음과 같은 오류로 실패했습니다:
```
Getting Pages deployment status...
Current status: updating_pages
Getting Pages deployment status...
Current status: updating_pages
Getting Pages deployment status...
Current status: updating_pages
Getting Pages deployment status...
Current status: updating_pages
Getting Pages deployment status...
```

배포가 "updating_pages" 상태에서 멈춘 후 결국 실패했습니다.

## 원인
문제의 원인은 사용자 정의 도메인(blog.bestf.net)을 구성하는 데 필요한 CNAME 파일이 저장소 루트에는 있었지만 `public` 디렉토리에는 없었기 때문입니다. Hugo는 `public` 디렉토리의 내용을 GitHub Pages에 배포하므로, CNAME 파일이 배포에 포함되지 않아 GitHub Pages가 사용자 정의 도메인을 구성하지 못했습니다.

## 해결책
해결책은 CNAME 파일을 `static` 디렉토리에 복사하는 것이었습니다. 이렇게 하면 Hugo가 빌드 과정에서 해당 파일을 `public` 디렉토리에 포함시킵니다.

```bash
mkdir -p static && cp CNAME static/
```

이렇게 하면 CNAME 파일이 배포된 사이트에 포함되어 GitHub Pages가 사용자 정의 도메인을 올바르게 구성할 수 있습니다.

## 검증
해결책을 구현한 후, 로컬 Hugo 빌드를 실행하여 CNAME 파일이 `public` 디렉토리에 포함되었는지 확인했습니다:

```bash
hugo
find public -name "CNAME"
# 출력: public/CNAME
```

이를 통해 해결책이 올바르게 작동하는 것을 확인했습니다.

## 추가 정보
- CNAME 파일에는 사용자 정의 도메인이 포함되어 있습니다: `blog.bestf.net`
- 이는 Hugo 구성의 `baseURL`과 일치합니다: `https://blog.bestf.net/`
- GitHub Actions 워크플로우는 사이트를 GitHub Pages에 배포하도록 구성되어 있습니다

이 해결책으로 GitHub Pages 배포가 이제 성공적으로 완료될 것입니다.