---
layout: page
title: Blog
permalink: /news/
---

<div class="link-grid">

{% for post in site.posts %}
  {% capture y %}{{post.date | date:"%Y"}}{% endcapture %}
  {% if year != y %}
    {% if year != nil %}
</div>
    {% endif %}
    {% assign year = y %}
<div class="link-grid-section">
  <h2>{{ y }}</h2>
  {% endif %}
  <a href="{{ post.url }}" title="{{ post.title }}">{{ post.date | date:"%b %-d" }} — {{ post.title }}</a>
{% endfor %}
{% if year != nil %}
</div>
{% endif %}

</div>
