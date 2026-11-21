---
layout: page
title: Talks
title_zh: 报告
permalink: /talks/
---

{% assign years = "2023,2022,2021,2019,2018,2017" | split: "," %}

<nav class="talk-year-nav" aria-labelledby="talk-year-nav-label">
  <span class="language-pair" id="talk-year-nav-label"><span class="en-only" lang="en">Jump to year</span><span class="zh-only" lang="zh-CN">按年份浏览</span></span>
  <ul role="list">
    {% for yr in years %}
    <li><a href="#talks-{{ yr }}">{{ yr }}</a></li>
    {% endfor %}
  </ul>
</nav>

{% for yr in years %}
{% assign data_file = "talk-" | append: yr %}
<section class="talk-group" aria-labelledby="talks-{{ yr }}">
  <h2 class="talk-year" id="talks-{{ yr }}">{{ yr }}</h2>
  <ul class="talk-list" role="list">
    {% for talk in site.data[data_file] %}
    <li class="talk-item">
      <div>
        <h3 class="talk-title">{{ talk.title | escape }}</h3>
        {% if talk.page or talk.URL %}
        <p class="talk-meta">
          {{ talk.page | escape }}
          {% if talk.URL %}{% if talk.page %}&mdash; {% endif %}<a href="{{ talk.URL | escape }}" target="_blank" rel="noopener">{{ talk.URL | escape }}</a>{% endif %}
        </p>
        {% endif %}
      </div>
      {% if talk.journal.abbreviation %}
      <span class="talk-type">{{ talk.journal.abbreviation | escape }}</span>
      {% endif %}
    </li>
    {% endfor %}
  </ul>
</section>
{% endfor %}
