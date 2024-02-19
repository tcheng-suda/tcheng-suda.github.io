---
layout: page
title: Publications
permalink: /publications/
---

## Journal Articles
|[**Google Scholar**](https://goo.gl/AgbNaK)
|[**ResearchGate**](https://www.researchgate.net/profile/Tao_Cheng13)
|[**ORCID**](http://orcid.org/0000-0003-4830-177X)
|[**Web of Science**](https://www.webofscience.com/wos/author/record/1444044/)
|  
|[**2023**](#2023)
|[**2022**](#2022)
|[**2021**](#2021)
|[**2020**](#2020)
|[**2019**](#2019)|[**2018**](#2018)|[**2017**](#2017)|[**2016**](#2016)
|[**2015**](#2015)|[**2014**](#2014)|[**before 2014**](#2014-b)|  

## <a name="Selected"></a>Selected
<div class='panel-pub'>
<ol start='5' reversed>
{% for article in site.data.representative %}
    <li>
    <div class="title">
    <span class="title">{{ article.title }}</span>
    {% if article.fulltext %}
        <a title="fulltext" href="{{ site.url }}/downloads/journal/{{ article.fulltext }}"><i class="fa fa-file-pdf-o"></i></a>
    {% endif %}
    </div>
    <div class='author'>
    {% for author in article.author %}
        <span class='{{ author.role }}'>{{ author.family }} {{ author.given_initial }}{% if author.role contains 'corr' %}*{% endif %}; </span>
    {% endfor %}
    </div>
    <div class="pubinfo">
    <span class="source">{{ article.journal.abbreviation }} </span><span class="year">{{ article.year }}, </span><span class="volume">{{ article.volume }}, </span><span class="page">{{ article.page }}.</span>{% if article.language != 'english' %}<span class="language"> (In {{ article.language }})</span>{% endif %}
    </div>
    <div class="url">
        <a href="{{ article.URL }}">{{ article.URL }}</a>
    </div>
    <div class="note">
        <span class="note">{{ article.note }}</span>
    </div>
    <div class="media1">
        <span class="media1">{{ article.media1}}</span>
    </div>
    <div class="media1_url">
        <a href="{{ article.media1_url}}">{{ article.media1_url}}</a>
    </div>
    {% if article.image_url%}
        <div class="image_url">
            <img src="{{ article.image_url}}" height="180" align="middle">
        </div>
    {% endif %}
    </li>
{% endfor %}
</ol>
</div>
<a href="#top">Back to top</a>

## <a name="2023"></a>2023

<div class='panel-pub'>
<ol start='188' reversed>
{% for article in site.data.pub-2023 %}
    <li>
    <div class="title">
    <span class="title">{{ article.title }}</span>
    {% if article.fulltext %}
        <a title="fulltext" href="{{ site.url }}/downloads/journal/{{ thesis.fulltext }}"><i class="fa fa-file-pdf-o"></i></a>
    {% endif %}
    </div>
    <div class='author'>
    {% for author in article.author %}
        <span class='{{ author.role }}'>{{ author.family }} {{ author.given_initial }}{% if author.role contains 'corr' %}*{% endif %}; </span>
    {% endfor %}
    </div>
    <div class="pubinfo">
    <span class="source">{{ article.journal.abbreviation }} </span><span class="year">{{ article.year }}, </span><span class="volume">{{ article.volume }}, </span><span class="page">{{ article.page }}.</span>{% if article.language != 'english' %}<span class="language"> (In {{ article.language }})</span>{% endif %}
    </div>
    <div class="url">
        <a href="{{ article.URL }}">{{ article.URL }}</a>
    </div>
    <div class="note">
        <span class="note">{{ article.note }}</span>
    </div>
    <div class="media1">
        <span class="media1">{{ article.media1}}</span>
    </div>
    <div class="media1_url">
        <a href="{{ article.media1_url}}">{{ article.media1_url}}</a>
    </div>
    {% if article.image_url%}
        <div class="image_url">
            <img src="{{ article.image_url}}" height="180" align="middle">
        </div>
    {% endif %}
    </li>
{% endfor %}
</ol>
</div>
<a href="#top">Back to top</a>

## <a name="2022"></a>2022

<div class='panel-pub'>
<ol start='153' reversed>
{% for article in site.data.pub-2022 %}
    <li>
    <div class="title">
    <span class="title">{{ article.title }}</span>
    {% if article.fulltext %}
        <a title="fulltext" href="{{ site.url }}/downloads/journal/{{ thesis.fulltext }}"><i class="fa fa-file-pdf-o"></i></a>
    {% endif %}
    </div>
    <div class='author'>
    {% for author in article.author %}
        <span class='{{ author.role }}'>{{ author.family }} {{ author.given_initial }}{% if author.role contains 'corr' %}*{% endif %}; </span>
    {% endfor %}
    </div>
    <div class="pubinfo">
    <span class="source">{{ article.journal.abbreviation }} </span><span class="year">{{ article.year }}, </span><span class="volume">{{ article.volume }}, </span><span class="page">{{ article.page }}.</span>{% if article.language != 'english' %}<span class="language"> (In {{ article.language }})</span>{% endif %}
    </div>
    <div class="url">
        <a href="{{ article.URL }}">{{ article.URL }}</a>
    </div>
    <div class="note">
        <span class="note">{{ article.note }}</span>
    </div>
    <div class="media1">
        <span class="media1">{{ article.media1}}</span>
    </div>
    <div class="media1_url">
        <a href="{{ article.media1_url}}">{{ article.media1_url}}</a>
    </div>
    {% if article.image_url%}
        <div class="image_url">
            <img src="{{ article.image_url}}" height="180" align="middle">
        </div>
    {% endif %}
    </li>
{% endfor %}
</ol>
</div>
<a href="#top">Back to top</a>

## <a name="2021"></a>2021

<div class='panel-pub'>
<ol start='129' reversed>
{% for article in site.data.pub-2021 %}
    <li>
    <div class="title">
    <span class="title">{{ article.title }}</span>
    {% if article.fulltext %}
        <a title="fulltext" href="{{ site.url }}/downloads/journal/{{ thesis.fulltext }}"><i class="fa fa-file-pdf-o"></i></a>
    {% endif %}
    </div>
    <div class='author'>
    {% for author in article.author %}
        <span class='{{ author.role }}'>{{ author.family }} {{ author.given_initial }}{% if author.role contains 'corr' %}*{% endif %}; </span>
    {% endfor %}
    </div>
    <div class="pubinfo">
    <span class="source">{{ article.journal.abbreviation }} </span><span class="year">{{ article.year }}, </span><span class="volume">{{ article.volume }}, </span><span class="page">{{ article.page }}.</span>{% if article.language != 'english' %}<span class="language"> (In {{ article.language }})</span>{% endif %}
    </div>
    <div class="url">
        <a href="{{ article.URL }}">{{ article.URL }}</a>
    </div>
    <div class="note">
        <span class="note">{{ article.note }}</span>
    </div>
    <div class="media1">
        <span class="media1">{{ article.media1}}</span>
    </div>
    <div class="media1_url">
        <a href="{{ article.media1_url}}">{{ article.media1_url}}</a>
    </div>
    {% if article.image_url%}
        <div class="image_url">
            <img src="{{ article.image_url}}" height="180" align="middle">
        </div>
    {% endif %}
    </li>
{% endfor %}
</ol>
</div>
<a href="#top">Back to top</a>

## <a name="2020"></a>2020

<div class='panel-pub'>
<ol start='76' reversed>
{% for article in site.data.pub-2020 %}
    <li>
    <div class="title">
    <span class="title">{{ article.title }}</span>
    {% if article.fulltext %}
        <a title="fulltext" href="{{ site.url }}/downloads/journal/{{ thesis.fulltext }}"><i class="fa fa-file-pdf-o"></i></a>
    {% endif %}
    </div>
    <div class='author'>
    {% for author in article.author %}
        <span class='{{ author.role }}'>{{ author.family }} {{ author.given_initial }}{% if author.role contains 'corr' %}*{% endif %}; </span>
    {% endfor %}
    </div>
    <div class="pubinfo">
    <span class="source">{{ article.journal.abbreviation }} </span><span class="year">{{ article.year }}, </span><span class="volume">{{ article.volume }}, </span><span class="page">{{ article.page }}.</span>{% if article.language != 'english' %}<span class="language"> (In {{ article.language }})</span>{% endif %}
    </div>
    <div class="url">
        <a href="{{ article.URL }}">{{ article.URL }}</a>
    </div>
    <div class="note">
        <span class="note">{{ article.note }}</span>
    </div>
    <div class="media1">
        <span class="media1">{{ article.media1}}</span>
    </div>
    <div class="media1_url">
        <a href="{{ article.media1_url}}">{{ article.media1_url}}</a>
    </div>
    {% if article.image_url%}
        <div class="image_url">
            <img src="{{ article.image_url}}" height="180" align="middle">
        </div>
    {% endif %}
    </li>
{% endfor %}
</ol>
</div>
<a href="#top">Back to top</a>

## <a name="2019"></a>2019

<div class='panel-pub'>
<ol start='62' reversed>
{% for article in site.data.pub-2019 %}
    <li>
    <div class="title">
    <span class="title">{{ article.title }}</span>
    {% if article.fulltext %}
        <a title="fulltext" href="{{ site.url }}/downloads/journal/{{ thesis.fulltext }}"><i class="fa fa-file-pdf-o"></i></a>
    {% endif %}
    </div>
    <div class='author'>
    {% for author in article.author %}
        <span class='{{ author.role }}'>{{ author.family }} {{ author.given_initial }}{% if author.role contains 'corr' %}*{% endif %}; </span>
    {% endfor %}
    </div>
    <div class="pubinfo">
    <span class="source">{{ article.journal.abbreviation }} </span><span class="year">{{ article.year }}, </span><span class="volume">{{ article.volume }}, </span><span class="page">{{ article.page }}.</span>{% if article.language != 'english' %}<span class="language"> (In {{ article.language }})</span>{% endif %}
    </div>
    <div class="url">
        <a href="{{ article.URL }}">{{ article.URL }}</a>
    </div>
    <div class="note">
        <span class="note">{{ article.note }}</span>
    </div>
    <div class="media1">
        <span class="media1">{{ article.media1}}</span>
    </div>
    <div class="media1_url">
        <a href="{{ article.media1_url}}">{{ article.media1_url}}</a>
    </div>
    {% if article.image_url%}
        <div class="image_url">
            <img src="{{ article.image_url}}" height="180" align="middle">
        </div>
    {% endif %}
    </li>
{% endfor %}
</ol>
</div>
<a href="#top">Back to top</a>

## <a name="2018"></a>2018

<div class='panel-pub'>
<ol start='48' reversed>
{% for article in site.data.pub-2018 %}
    <li>
    <div class="title">
    <span class="title">{{ article.title }}</span>
    {% if article.fulltext %}
        <a title="fulltext" href="{{ site.url }}/downloads/journal/{{ thesis.fulltext }}"><i class="fa fa-file-pdf-o"></i></a>
    {% endif %}
    </div>
    <div class='author'>
    {% for author in article.author %}
        <span class='{{ author.role }}'>{{ author.family }} {{ author.given_initial }}{% if author.role contains 'corr' %}*{% endif %}; </span>
    {% endfor %}
    </div>
    <div class="pubinfo">
    <span class="source">{{ article.journal.abbreviation }} </span><span class="year">{{ article.year }}, </span><span class="volume">{{ article.volume }}, </span><span class="page">{{ article.page }}.</span>{% if article.language != 'english' %}<span class="language"> (In {{ article.language }})</span>{% endif %}
    </div>
    <div class="url">
        <a href="{{ article.URL }}">{{ article.URL }}</a>
    </div>
    <div class="note">
        <span class="note">{{ article.note }}</span>
    </div>
    <div class="media1">
        <span class="media1">{{ article.media1}}</span>
    </div>
    <div class="media1_url">
        <a href="{{ article.media1_url}}">{{ article.media1_url}}</a>
    </div>
    {% if article.image_url%}
        <div class="image_url">
            <img src="{{ article.image_url}}" height="180" align="middle">
        </div>
    {% endif %}
    </li>
{% endfor %}
</ol>
</div>
<a href="#top">Back to top</a>

## <a name="2017"></a>2017

<div class='panel-pub'>
<ol start='36' reversed>
{% for article in site.data.pub-2017 %}
    <li>
    <div class="title">
    <span class="title">{{ article.title }}</span>
    {% if article.fulltext %}
        <a title="fulltext" href="{{ site.url }}/downloads/journal/{{ thesis.fulltext }}"><i class="fa fa-file-pdf-o"></i></a>
    {% endif %}
    </div>
    <div class='author'>
    {% for author in article.author %}
        <span class='{{ author.role }}'>{{ author.family }} {{ author.given_initial }}{% if author.role contains 'corr' %}*{% endif %}; </span>
    {% endfor %}
    </div>
    <div class="pubinfo">
    <span class="source">{{ article.journal.abbreviation }} </span><span class="year">{{ article.year }}, </span><span class="volume">{{ article.volume }}, </span><span class="page">{{ article.page }}.</span>{% if article.language != 'english' %}<span class="language"> (In {{ article.language }})</span>{% endif %}
    </div>
    <div class="url">
        <a href="{{ article.URL }}">{{ article.URL }}</a>
    </div>
    <div class="note">
        <span class="note">{{ article.note }}</span>
    </div>
    <div class="media1">
        <span class="media1">{{ article.media1}}</span>
    </div>
    <div class="media1_url">
        <a href="{{ article.media1_url}}">{{ article.media1_url}}</a>
    </div>
    {% if article.image_url%}
        <div class="image_url">
            <img src="{{ article.image_url}}" height="180" align="middle">
        </div>
    {% endif %}
    </li>
{% endfor %}
</ol>
</div>
<a href="#top">Back to top</a>

## <a name="2016"></a>2016

<div class='panel-pub'>
<ol start='21' reversed>
{% for article in site.data.pub-2016 %}
    <li>
    <div class="title">
    <span class="title">{{ article.title }}</span>
    {% if article.fulltext %}
        <a title="fulltext" href="{{ site.url }}/downloads/journal/{{ thesis.fulltext }}"><i class="fa fa-file-pdf-o"></i></a>
    {% endif %}
    </div>
    <div class='author'>
    {% for author in article.author %}
        <span class='{{ author.role }}'>{{ author.family }} {{ author.given_initial }}{% if author.role contains 'corr' %}*{% endif %}; </span>
    {% endfor %}
    </div>
    <div class="pubinfo">
    <span class="source">{{ article.journal.abbreviation }} </span><span class="year">{{ article.year }}, </span><span class="volume">{{ article.volume }}, </span><span class="page">{{ article.page }}.</span>{% if article.language != 'english' %}<span class="language"> (In {{ article.language }})</span>{% endif %}
    </div>
    <div class="url">
        <a href="{{ article.URL }}">{{ article.URL }}</a>
    </div>
    <div class="note">
        <span class="note">{{ article.note }}</span>
    </div>
    <div class="media1">
        <span class="media1">{{ article.media1}}</span>
    </div>
    <div class="media1_url">
        <a href="{{ article.media1_url}}">{{ article.media1_url}}</a>
    </div>
    {% if article.image_url%}
        <div class="image_url">
            <img src="{{ article.image_url}}" height="180" align="middle">
        </div>
    {% endif %}
    </li>
{% endfor %}
</ol>
</div>
<a href="#top">Back to top</a>

## <a name="2015"></a>2015

<div class='panel-pub'>
<ol start='17' reversed>
{% for article in site.data.pub-2015 %}
    <li>
    <div class="title">
    <span class="title">{{ article.title }}</span>
    {% if article.fulltext %}
        <a title="fulltext" href="{{ site.url }}/downloads/journal/{{ thesis.fulltext }}"><i class="fa fa-file-pdf-o"></i></a>
    {% endif %}
    </div>
    <div class='author'>
    {% for author in article.author %}
        <span class='{{ author.role }}'>{{ author.family }} {{ author.given_initial }}{% if author.role contains 'corr' %}*{% endif %}; </span>
    {% endfor %}
    </div>
    <div class="pubinfo">
    <span class="source">{{ article.journal.abbreviation }} </span><span class="year">{{ article.year }}, </span><span class="volume">{{ article.volume }}, </span><span class="page">{{ article.page }}.</span>{% if article.language != 'english' %}<span class="language"> (In {{ article.language }})</span>{% endif %}
    </div>
    <div class="url">
        <a href="{{ article.URL }}">{{ article.URL }}</a>
    </div>
    <div class="note">
        <span class="note">{{ article.note }}</span>
    </div>
    <div class="media1">
        <span class="media1">{{ article.media1}}</span>
    </div>
    <div class="media1_url">
        <a href="{{ article.media1_url}}">{{ article.media1_url}}</a>
    </div>
    {% if article.image_url%}
        <div class="image_url">
            <img src="{{ article.image_url}}" height="180" align="middle">
        </div>
    {% endif %}
    </li>
{% endfor %}
</ol>
</div>
<a href="#top">Back to top</a>

## <a name="2014"></a>2014

<div class='panel-pub'>
<ol start='10' reversed>
{% for article in site.data.pub-2014 %}
    <li>
    <div class="title">
    <span class="title">{{ article.title }}</span>
    {% if article.fulltext %}
        <a title="fulltext" href="{{ site.url }}/downloads/journal/{{ thesis.fulltext }}"><i class="fa fa-file-pdf-o"></i></a>
    {% endif %}
    </div>
    <div class='author'>
    {% for author in article.author %}
        <span class='{{ author.role }}'>{{ author.family }} {{ author.given_initial }}{% if author.role contains 'corr' %}*{% endif %}; </span>
    {% endfor %}
    </div>
    <div class="pubinfo">
    <span class="source">{{ article.journal.abbreviation }} </span><span class="year">{{ article.year }}, </span><span class="volume">{{ article.volume }}, </span><span class="page">{{ article.page }}.</span>{% if article.language != 'english' %}<span class="language"> (In {{ article.language }})</span>{% endif %}
    </div>
    <div class="url">
        <a href="{{ article.URL }}">{{ article.URL }}</a>
    </div>
    <div class="note">
        <span class="note">{{ article.note }}</span>
    </div>
    <div class="media1">
        <span class="media1">{{ article.media1}}</span>
    </div>
    <div class="media1_url">
        <a href="{{ article.media1_url}}">{{ article.media1_url}}</a>
    </div>
    {% if article.image_url%}
        <div class="image_url">
            <img src="{{ article.image_url}}" height="180" align="middle">
        </div>
    {% endif %}
    </li>
{% endfor %}
</ol>
</div>
<a href="#top">Back to top</a>

## <a name="2014-b"></a>before 2014

<div class='panel-pub'>
<ol start='6' reversed>
{% for article in site.data.pub-2014-b %}
    <li>
    <div class="title">
    <span class="title">{{ article.title }}</span>
    {% if article.fulltext %}
        <a title="fulltext" href="{{ site.url }}/downloads/journal/{{ thesis.fulltext }}"><i class="fa fa-file-pdf-o"></i></a>
    {% endif %}
    </div>
    <div class='author'>
    {% for author in article.author %}
        <span class='{{ author.role }}'>{{ author.family }} {{ author.given_initial }}{% if author.role contains 'corr' %}*{% endif %}; </span>
    {% endfor %}
    </div>
    <div class="pubinfo">
    <span class="source">{{ article.journal.abbreviation }} </span><span class="year">{{ article.year }}, </span><span class="volume">{{ article.volume }}, </span><span class="page">{{ article.page }}.</span>{% if article.language != 'english' %}<span class="language"> (In {{ article.language }})</span>{% endif %}
    </div>
    <div class="url">
        <a href="{{ article.URL }}">{{ article.URL }}</a>
    </div>
    <div class="note">
        <span class="note">{{ article.note }}</span>
    </div>
    <div class="media1">
        <span class="media1">{{ article.media1}}</span>
    </div>
    <div class="media1_url">
        <a href="{{ article.media1_url}}">{{ article.media1_url}}</a>
    </div>
    {% if article.image_url%}
        <div class="image_url">
            <img src="{{ article.image_url}}" height="180" align="middle">
        </div>
    {% endif %}
    </li>
{% endfor %}
</ol>
</div>
<a href="#top">Back to top</a>
