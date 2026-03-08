---
layout: default
title: Home
---

<h2>Latest Posts</h2>

<div class="post-grid">
{% for post in site.posts %}
  <div class="post-card">

    {% if post.image %}
    <img src="{{ post.image }}" class="post-thumb">
    {% endif %}

	<small>{{ post.date | date: "%B %d, %Y" }}</small>
	
    <h3>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </h3>

    <p>{{ post.excerpt }}</p>

  </div>
{% endfor %}
</div>