---
layout: default
title: Home
---

# 안녕하세요 👋

여기는 꿈돌이 블로그 입니다.  
Jekyll + GitHub Pages 기반으로 운영되고 있습니다.
-  글 쓰기 연습을 하고자 만들어 보았습니다. 
- obsidian 를 사용하여 글 작성을 합니다. 

# ✍️ 최신 글
<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a> - {{ post.date | date: "%Y-%m-%d" }}
    </li>
  {% endfor %}
</ul>
