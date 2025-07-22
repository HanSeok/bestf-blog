---
title: "categories nav  설정 "
date: 2025-07-22T10:32:00+09:00
draft: false
tags: 
  - dev
  - hugo
  - menu
categories:
  - dev
  - hugo
layout: post
---

```text
메뉴의 카테고리를 생성하는 데이터가 
배열형태로 사용하면 좋을것 같은데 좋은 구조로 만들어져 있지 않아서
코드를 확인하기 위해 AI 에게 문의했다. 

이후  chatgpt  를 사용해서 코드를 변경까지 완료 
```

### parent_categories.yaml 파일의 사용처 및 동작 방식

`parent_categories.yaml` 파일은 블로그의 계층적 카테고리 시스템에서 부모-자식 카테고리 관계를 정의하는 데 사용됩니다. 이 파일은 다음과 같은 방식으로 작동합니다:

### 파일 구조 및 역할

`parent_categories.yaml` 파일은 `/data/` 디렉토리에 위치하며 다음과 같은 형식으로 구성됩니다:
```yaml
# 형식: 자식카테고리: 부모카테고리
기초: 선상낚시
한치: 선상낚시
github: dev
hugo: dev
jekyll: dev
junie: dev
default: 미분류
```

각 줄은 `자식카테고리: 부모카테고리` 형식으로 부모-자식 관계를 정의합니다.

### 사용되는 코드

이 파일은 주로 `/layouts/partials/process-categories.html` 템플릿에서 사용됩니다. 이 템플릿은 다음과 같은 작업을 수행합니다:

1. 슬래시(/) 표기법을 사용한 카테고리를 처리합니다 (예: "선상낚시/기초").
2. `parent_categories.yaml`에 정의된 부모-자식 관계를 처리합니다.
3. 이 정보를 바탕으로 계층적 카테고리 데이터 구조를 생성합니다.

관련 코드 부분:
```html
{{ range $child, $parent := site.Data.parent_categories }}
  {{ if not (isset $relationships $child) }}
    {{ $relationships = merge $relationships (dict $child $parent) }}
  {{ end }}
  
  {{ if not (in $parentCategories $parent) }}
    {{ $parentCategories = $parentCategories | append $parent }}
  {{ end }}
  
  {{ if not (isset $childCategories $parent) }}
    {{ $childCategories = merge $childCategories (dict $parent (slice $child)) }}
  {{ else }}
    {{ $children := index $childCategories $parent }}
    {{ if not (in $children $child) }}
      {{ $children = $children | append $child }}
      {{ $childCategories = merge $childCategories (dict $parent $children) }}
    {{ end }}
  {{ end }}
{{ end }}
```

### 사용되는 위치

이 처리된 카테고리 데이터는 다음 파일들에서 사용됩니다:

1. `/layouts/partials/nav.html`: 네비게이션 메뉴에서 계층적 카테고리를 표시합니다.
2. `/layouts/taxonomy/category.html`: 개별 카테고리 페이지에서 부모-자식 관계를 표시합니다.
3. `/layouts/taxonomy/category.terms.html`: 카테고리 목록 페이지에서 계층 구조를 표시합니다.

### 카테고리 지정 방법

블로그 포스트에 카테고리를 지정하는 방법에는 두 가지가 있습니다:

#### 방법 1: 개별 카테고리 항목 사용
```yaml
---
title: "포스트 제목"
categories:
  - 부모카테고리
  - 자식카테고리
---
```
이 방법을 사용할 경우, `parent_categories.yaml` 파일에 부모-자식 관계를 명시적으로 정의해야 합니다.

#### 방법 2: 슬래시(/) 표기법 사용
```yaml
---
title: "포스트 제목"
categories:
  - 부모카테고리/자식카테고리
---
```
이 방법을 사용하면 `parent_categories.yaml` 파일에 관계를 별도로 정의하지 않아도 자동으로 계층 구조가 생성됩니다.

### 동작 방식 요약

1. `process-categories.html` 템플릿이 모든 카테고리를 검사합니다.
2. 슬래시(/)가 포함된 카테고리를 발견하면, 이를 부모와 자식 부분으로 분리합니다.
3. `parent_categories.yaml` 파일에서 정의된 관계를 처리합니다.
4. 이 정보를 바탕으로 계층적 카테고리 데이터 구조를 생성합니다.
5. 이 데이터 구조는 네비게이션 메뉴와 카테고리 페이지에서 계층적 카테고리를 표시하는 데 사용됩니다.

이 시스템을 통해 블로그에서 2단계 깊이의 계층적 카테고리를 효과적으로 관리하고 표시할 수 있습니다.