---
title: "Junie와 함께-menu-categories수정작업"
date: 2025-07-21T16:48:00+09:00
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

# 계층적 카테고리 시스템 사용 가이드

이 문서는 블로그에서 2단계 깊이의 계층적 카테고리를 사용하는 방법을 설명합니다.

## 개요

블로그 포스트에 카테고리를 지정할 때 계층 구조(부모-자식 관계)를 사용할 수 있습니다. 예를 들어:

- 낚시 (부모 카테고리)
  - 기초 (자식 카테고리)
  - 장비 (자식 카테고리)
  - 기법 (자식 카테고리)

이 시스템을 사용하면 카테고리 페이지에서 계층 구조가 시각적으로 표시되며, 부모 카테고리 페이지에서는 모든 자식 카테고리 목록이 표시되고, 자식 카테고리 페이지에서는 부모 카테고리로의 링크가 표시됩니다.

## 사용 방법

### 1. 포스트에 카테고리 지정하기

포스트의 front matter에서 카테고리를 지정하는 방법에는 두 가지가 있습니다:

#### 방법 1: 개별 카테고리 항목 사용 (기본 방식)

```yaml
---
title: "포스트 제목"
date: 2025-07-21T15:32:00+09:00
categories:
  - 부모카테고리
  - 자식카테고리
---
```

예를 들어, "낚시" 카테고리의 "기초" 하위 카테고리에 포스트를 지정하려면:

```yaml
---
title: "낚시 입문 가이드"
date: 2025-07-21T15:32:00+09:00
categories:
  - 낚시
  - 기초
---
```

#### 방법 2: 슬래시(/) 표기법 사용 (간편 방식)

슬래시(/)를 사용하여 부모/자식 관계를 직접 표현할 수 있습니다:

```yaml
---
title: "포스트 제목"
date: 2025-07-21T15:32:00+09:00
categories:
  - 부모카테고리/자식카테고리
---
```

예를 들어, "낚시" 카테고리의 "기초" 하위 카테고리에 포스트를 지정하려면:

```yaml
---
title: "낚시 입문 가이드"
date: 2025-07-21T15:32:00+09:00
categories:
  - 낚시/기초
---
```

이 방식을 사용하면 `parent_categories.yaml` 파일에 관계를 별도로 정의하지 않아도 자동으로 계층 구조가 생성됩니다.

### 2. 부모-자식 관계 정의하기

#### 방법 1을 사용하는 경우 (개별 카테고리 항목)

개별 카테고리 항목을 사용하는 경우, 부모-자식 관계를 `/data/parent_categories.yaml` 파일에 정의해야 합니다. 이 파일의 형식은 다음과 같습니다:

```yaml
# 형식: 자식카테고리: 부모카테고리
자식카테고리1: 부모카테고리1
자식카테고리2: 부모카테고리1
자식카테고리3: 부모카테고리2
```

예를 들어:

```yaml
기초: 낚시
장비: 낚시
기법: 낚시
프론트엔드: 개발
백엔드: 개발
```

#### 방법 2를 사용하는 경우 (슬래시 표기법)

슬래시(/) 표기법을 사용하는 경우, 시스템이 자동으로 부모-자식 관계를 인식하므로 `parent_categories.yaml` 파일에 별도로 정의할 필요가 없습니다. 그러나 두 방식을 혼합해서 사용하는 경우, 이 파일은 여전히 참조됩니다.

### 3. 카테고리 페이지 확인하기

설정이 완료되면 다음과 같은 URL에서 카테고리 페이지를 확인할 수 있습니다:

- 모든 카테고리 목록: `/categories/`
- 특정 카테고리 페이지: `/categories/카테고리이름/`

## 작동 방식

이 시스템은 다음과 같은 구성 요소로 이루어져 있습니다:

1. **데이터 파일**: `/data/parent_categories.yaml`에 부모-자식 카테고리 관계를 정의합니다 (방법 1 사용 시).
2. **템플릿 파일**:
   - `/layouts/partials/process-categories.html`: 카테고리 처리 및 슬래시 표기법 해석을 위한 부분 템플릿
   - `/layouts/taxonomy/category.html`: 개별 카테고리 페이지 템플릿
   - `/layouts/taxonomy/category.terms.html`: 카테고리 목록 페이지 템플릿
3. **CSS 파일**: `/assets/css/categories.css`에 계층적 카테고리 표시를 위한 스타일을 정의합니다.

### 슬래시 표기법 처리 방식

슬래시(/) 표기법을 사용하면 다음과 같은 과정으로 처리됩니다:

1. `process-categories.html` 부분 템플릿이 모든 카테고리를 검사합니다.
2. 슬래시(/)가 포함된 카테고리를 발견하면, 이를 부모와 자식 부분으로 분리합니다.
3. 부모 카테고리와 자식 카테고리를 각각 별도의 카테고리로 등록합니다.
4. 부모-자식 관계를 내부적으로 설정하여 계층 구조를 형성합니다.
5. 이 관계는 카테고리 페이지에서 표시될 때 사용됩니다.

이 방식을 통해 사용자는 `parent_categories.yaml` 파일을 직접 수정하지 않고도 계층적 카테고리를 쉽게 사용할 수 있습니다.

## 메뉴에서의 계층적 카테고리

블로그의 메인 메뉴에는 계층적 카테고리가 표시됩니다. 이 기능은 다음과 같은 특징을 가지고 있습니다:

1. **계층 구조 표시**: 부모 카테고리와 그 아래 자식 카테고리가 계층적으로 표시됩니다.
2. **포스트 수 표시**: 각 카테고리 옆에 해당 카테고리에 속한 포스트의 수가 괄호 안에 표시됩니다.
3. **시각적 구분**: 부모 카테고리는 굵은 글씨와 주요 색상으로 표시되며, 자식 카테고리는 들여쓰기와 세로선으로 구분됩니다.

예를 들어:

```
카테고리
낚시 (3)
  ├─ 기초 (1)
  └─ 장비 (2)
개발 (5)
  ├─ 프론트엔드 (2)
  └─ 백엔드 (3)
여행 (2)
```

이 메뉴는 `/layouts/partials/nav.html` 템플릿에서 구현되며, 계층적 카테고리 데이터는 `process-categories.html` 부분 템플릿을 통해 처리됩니다. 스타일은 `/assets/css/categories.css` 파일에 정의되어 있습니다.

## 주의사항

- 카테고리 이름에는 공백이 포함될 수 있지만, URL에서는 소문자와 하이픈으로 변환됩니다.
- 한 포스트는 여러 카테고리에 속할 수 있으며, 각 카테고리는 서로 다른 계층 구조에 속할 수 있습니다.
- 3단계 이상의 깊이는 현재 지원되지 않습니다.
- 포스트 수는 해당 카테고리에 직접 속한 포스트의 수만 계산합니다. 자식 카테고리의 포스트는 포함되지 않습니다.
- **대소문자 주의**: `parent_categories.yaml` 파일에서 카테고리 이름의 대소문자는 Hugo가 HTML에서 사용하는 대소문자와 정확히 일치해야 합니다. 예를 들어, 포스트에서 `dev`로 정의했지만 Hugo가 `Dev`로 표시한다면, `parent_categories.yaml` 파일에서도 `Dev`로 사용해야 합니다. 그렇지 않으면 부모-자식 관계가 제대로 표시되지 않을 수 있습니다.