---
layout: page
title: Talks
permalink: /talks/
---

{% assign years = "2023,2022,2021,2019,2018,2017" | split: "," %}

{% for yr in years %}
<h2 class="talk-year">{{ yr }}</h2>
<ul class="talk-list">
{% assign data_file = "talk-" | append: yr %}
{% for talk in site.data[data_file] %}
  <li class="talk-item">
    <div class="talk-title">{{ talk.title }}</div>
    <div class="talk-meta">
      <span class="talk-type">{{ talk.journal.abbreviation }}</span>
      {{ talk.page }}{% if talk.URL %} &mdash; <a href="{{ talk.URL }}" target="_blank">{{ talk.URL }}</a>{% endif %}
    </div>
  </li>
{% endfor %}
</ul>
{% endfor %}
