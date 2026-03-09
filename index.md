---
layout: default
title: Home
---


<div class="post-grid">

{% for post in site.posts %}

<article class="post-card">

{% if post.image %}
<img src="{{ post.image }}" class="post-card-image">
{% endif %}

<div class="post-card-content">

<div class="post-card-category">
{% for category in post.categories %}
<span>{{ category }}</span>
{% endfor %}
</div>

<h2 class="post-card-title">
<a href="{{ post.url }}">{{ post.title }}</a>
</h2>

<p class="post-card-excerpt">
{{ post.excerpt }}
</p>

<p class="post-card-date">
{{ post.date | date: "%B %d, %Y" }}
</p>

</div>

</article>

{% endfor %}

</div>