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
    <li style="margin-bottom: 2em;">
      {% if post.thumbnail %}
        <img src="{{ post.thumbnail }}" alt="thumb" style="width: 200px;">
      {% endif %}

      <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
      <p><strong>작성일:</strong> {{ post.date | date: "%Y-%m-%d" }}</p>

      {% if post.categories %}
        <p><strong>카테고리:</strong> {{ post.categories | join: ", " }}</p>
      {% endif %}

      {% if post.tags %}
        <p><strong>태그:</strong> 
          {% for tag in post.tags %}
            <code>{{ tag }}</code>
          {% endfor %}
        </p>
      {% endif %}
    </li>
  {% endfor %}
</ul>