---
layout: page
title: Publications
permalink: /publications/
---
\|[**Google Scholar**](https://goo.gl/AgbNaK){:target="_blank" rel="noopener noreferrer"}
\|[**ResearchGate**](https://www.researchgate.net/profile/Tao_Cheng13){:target="_blank" rel="noopener noreferrer"}
\|[**ORCID**](http://orcid.org/0000-0003-4830-177X){:target="_blank" rel="noopener noreferrer"}
\|[**Web of Science**](https://www.webofscience.com/wos/author/record/1444044){:target="_blank" rel="noopener noreferrer"} \|  
|(citation:22,713; h-index:76; i10-index: 201 updated by April 4 2026)
|  
{% if jekyll.environment == 'production' %}{% assign local = false %}{% else %}{% assign local = true %}{% endif %}
|[**26{% if local %}-22{% endif %}**](#2026)
|[**25{% if local %}-34{% endif %}**](#2025)
|[**24{% if local %}-30{% endif %}**](#2024)
|[**23{% if local %}-26{% endif %}**](#2023)
|[**22{% if local %}-29{% endif %}**](#2022)
|[**21{% if local %}-29{% endif %}**](#2021)
|[**20{% if local %}-14{% endif %}**](#2020)
|[**19{% if local %}-14{% endif %}**](#2019)
|[**18{% if local %}-11{% endif %}**](#2018)
|[**17{% if local %}-15{% endif %}**](#2017)
|[**16{% if local %}-4{% endif %}**](#2016)
|[**15{% if local %}-7{% endif %}**](#2015)
|[**14{% if local %}-4{% endif %}**](#2014)
|[**before{% if local %}-6{% endif %}**](#2014-b)|  
Please send an email to [tcheng@suda.edu.cn](mailto:tcheng@suda.edu.cn), if full text is needed.  

## <a name="Selected"></a>Selected
<div class='panel-pub'>
<ol start='10' reversed>
{% for article in site.data.representative %}
    <li>
    <div class="title">
    {% if article.fulltext %}
        <a title="fulltext" href="{{ site.url }}/pdf/{{ article.fulltext }}" target="_blank"><i class="fa fa-file-pdf-o"></i></a>
    {% endif %}
    <span class="title">{{ article.title }}</span>
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
        <a href="{{ article.URL }}" target="_blank">{{ article.URL }}</a>
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

## <a name="2026"></a>2026

{% comment %} Publication numbering: auto-computed so each paper keeps a stable
   number and new papers take the next highest number. pub_base starts at
   (total article count across all years) + 1; the +1 accounts for the
   reversed <ol> convention where start is the highest item number. Do not
   edit the per-year start values below by hand — they are derived from
   pub_base. To add a new paper, just append it to the right year's data
   file; numbers adjust automatically. {% endcomment %}
{% assign pub_base = site.data.pub-2026.size %}
{% assign pub_base = pub_base | plus: site.data.pub-2025.size %}
{% assign pub_base = pub_base | plus: site.data.pub-2024.size %}
{% assign pub_base = pub_base | plus: site.data.pub-2023.size %}
{% assign pub_base = pub_base | plus: site.data.pub-2022.size %}
{% assign pub_base = pub_base | plus: site.data.pub-2021.size %}
{% assign pub_base = pub_base | plus: site.data.pub-2020.size %}
{% assign pub_base = pub_base | plus: site.data.pub-2019.size %}
{% assign pub_base = pub_base | plus: site.data.pub-2018.size %}
{% assign pub_base = pub_base | plus: site.data.pub-2017.size %}
{% assign pub_base = pub_base | plus: site.data.pub-2016.size %}
{% assign pub_base = pub_base | plus: site.data.pub-2015.size %}
{% assign pub_base = pub_base | plus: site.data.pub-2014.size %}
{% assign pub_base = pub_base | plus: site.data.pub-2014-b.size %}
{% assign pub_base = pub_base | plus: 1 %}
{% assign start_2026 = pub_base | minus: 1 %}
{% assign pub_base = pub_base | minus: site.data.pub-2026.size %}
<div class='panel-pub'>
<ol start='{{ start_2026 }}' reversed>
{% for article in site.data.pub-2026 %}
    <li>
    <div class="title">
    {% if article.fulltext %}
        <a title="fulltext" href="{{ site.url }}/pdf/{{ article.fulltext }}" target="_blank"><i class="fa fa-file-pdf-o"></i></a>
    {% endif %}
    <span class="title">{{ article.title }}</span>
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
        <a href="{{ article.URL }}" target="_blank">{{ article.URL }}</a>
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

## <a name="2025"></a>2025

{% assign start_2025 = pub_base | minus: 1 %}
{% assign pub_base = pub_base | minus: site.data.pub-2025.size %}
<div class='panel-pub'>
<ol start='{{ start_2025 }}' reversed>
{% for article in site.data.pub-2025 %}
    <li>
    <div class="title">
    {% if article.fulltext %}
        <a title="fulltext" href="{{ site.url }}/pdf/{{ article.fulltext }}" target="_blank"><i class="fa fa-file-pdf-o"></i></a>
    {% endif %}
    <span class="title">{{ article.title }}</span>
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
        <a href="{{ article.URL }}" target="_blank">{{ article.URL }}</a>
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

## <a name="2024"></a>2024

{% assign start_2024 = pub_base | minus: 1 %}
{% assign pub_base = pub_base | minus: site.data.pub-2024.size %}
<div class='panel-pub'>
<ol start='{{ start_2024 }}' reversed>
{% for article in site.data.pub-2024 %}
    <li>
    <div class="title">
    {% if article.fulltext %}
        <a title="fulltext" href="{{ site.url }}/pdf/{{ article.fulltext }}" target="_blank"><i class="fa fa-file-pdf-o"></i></a>
    {% endif %}
    <span class="title">{{ article.title }}</span>
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
        <a href="{{ article.URL }}" target="_blank">{{ article.URL }}</a>
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

{% assign start_2023 = pub_base | minus: 1 %}
{% assign pub_base = pub_base | minus: site.data.pub-2023.size %}
<div class='panel-pub'>
<ol start='{{ start_2023 }}' reversed>
{% for article in site.data.pub-2023 %}
    <li>
    <div class="title">
    {% if article.fulltext %}
        <a title="fulltext" href="{{ site.url }}/pdf/{{ article.fulltext }}" target="_blank"><i class="fa fa-file-pdf-o"></i></a>
    {% endif %}
    <span class="title">{{ article.title }}</span>
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
        <a href="{{ article.URL }}" target="_blank">{{ article.URL }}</a>
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

{% assign start_2022 = pub_base | minus: 1 %}
{% assign pub_base = pub_base | minus: site.data.pub-2022.size %}
<div class='panel-pub'>
<ol start='{{ start_2022 }}' reversed>
{% for article in site.data.pub-2022 %}
    <li>
    <div class="title">
    {% if article.fulltext %}
        <a title="fulltext" href="{{ site.url }}/pdf/{{ article.fulltext }}" target="_blank"><i class="fa fa-file-pdf-o"></i></a>
    {% endif %}
    <span class="title">{{ article.title }}</span>
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
        <a href="{{ article.URL }}" target="_blank">{{ article.URL }}</a>
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

{% assign start_2021 = pub_base | minus: 1 %}
{% assign pub_base = pub_base | minus: site.data.pub-2021.size %}
<div class='panel-pub'>
<ol start='{{ start_2021 }}' reversed>
{% for article in site.data.pub-2021 %}
    <li>
    <div class="title">
    {% if article.fulltext %}
        <a title="fulltext" href="{{ site.url }}/pdf/{{ article.fulltext }}" target="_blank"><i class="fa fa-file-pdf-o"></i></a>
    {% endif %}
    <span class="title">{{ article.title }}</span>
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
        <a href="{{ article.URL }}" target="_blank">{{ article.URL }}</a>
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

{% assign start_2020 = pub_base | minus: 1 %}
{% assign pub_base = pub_base | minus: site.data.pub-2020.size %}
<div class='panel-pub'>
<ol start='{{ start_2020 }}' reversed>
{% for article in site.data.pub-2020 %}
    <li>
    <div class="title">
    {% if article.fulltext %}
        <a title="fulltext" href="{{ site.url }}/pdf/{{ article.fulltext }}" target="_blank"><i class="fa fa-file-pdf-o"></i></a>
    {% endif %}
    <span class="title">{{ article.title }}</span>
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
        <a href="{{ article.URL }}" target="_blank">{{ article.URL }}</a>
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

{% assign start_2019 = pub_base | minus: 1 %}
{% assign pub_base = pub_base | minus: site.data.pub-2019.size %}
<div class='panel-pub'>
<ol start='{{ start_2019 }}' reversed>
{% for article in site.data.pub-2019 %}
    <li>
    <div class="title">
    {% if article.fulltext %}
        <a title="fulltext" href="{{ site.url }}/pdf/{{ article.fulltext }}" target="_blank"><i class="fa fa-file-pdf-o"></i></a>
    {% endif %}
    <span class="title">{{ article.title }}</span>
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
        <a href="{{ article.URL }}" target="_blank">{{ article.URL }}</a>
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

{% assign start_2018 = pub_base | minus: 1 %}
{% assign pub_base = pub_base | minus: site.data.pub-2018.size %}
<div class='panel-pub'>
<ol start='{{ start_2018 }}' reversed>
{% for article in site.data.pub-2018 %}
    <li>
    <div class="title">
    {% if article.fulltext %}
        <a title="fulltext" href="{{ site.url }}/pdf/{{ article.fulltext }}" target="_blank"><i class="fa fa-file-pdf-o"></i></a>
    {% endif %}
    <span class="title">{{ article.title }}</span>
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
        <a href="{{ article.URL }}" target="_blank">{{ article.URL }}</a>
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

{% assign start_2017 = pub_base | minus: 1 %}
{% assign pub_base = pub_base | minus: site.data.pub-2017.size %}
<div class='panel-pub'>
<ol start='{{ start_2017 }}' reversed>
{% for article in site.data.pub-2017 %}
    <li>
    <div class="title">
    {% if article.fulltext %}
        <a title="fulltext" href="{{ site.url }}/pdf/{{ article.fulltext }}" target="_blank"><i class="fa fa-file-pdf-o"></i></a>
    {% endif %}
    <span class="title">{{ article.title }}</span>
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
        <a href="{{ article.URL }}" target="_blank">{{ article.URL }}</a>
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

{% assign start_2016 = pub_base | minus: 1 %}
{% assign pub_base = pub_base | minus: site.data.pub-2016.size %}
<div class='panel-pub'>
<ol start='{{ start_2016 }}' reversed>
{% for article in site.data.pub-2016 %}
    <li>
    <div class="title">
    {% if article.fulltext %}
        <a title="fulltext" href="{{ site.url }}/pdf/{{ article.fulltext }}" target="_blank"><i class="fa fa-file-pdf-o"></i></a>
    {% endif %}
    <span class="title">{{ article.title }}</span>
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
        <a href="{{ article.URL }}" target="_blank">{{ article.URL }}</a>
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

{% assign start_2015 = pub_base | minus: 1 %}
{% assign pub_base = pub_base | minus: site.data.pub-2015.size %}
<div class='panel-pub'>
<ol start='{{ start_2015 }}' reversed>
{% for article in site.data.pub-2015 %}
    <li>
    <div class="title">
    {% if article.fulltext %}
        <a title="fulltext" href="{{ site.url }}/pdf/{{ article.fulltext }}" target="_blank"><i class="fa fa-file-pdf-o"></i></a>
    {% endif %}
    <span class="title">{{ article.title }}</span>
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
        <a href="{{ article.URL }}" target="_blank">{{ article.URL }}</a>
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

{% assign start_2014 = pub_base | minus: 1 %}
{% assign pub_base = pub_base | minus: site.data.pub-2014.size %}
<div class='panel-pub'>
<ol start='{{ start_2014 }}' reversed>
{% for article in site.data.pub-2014 %}
    <li>
    <div class="title">
    {% if article.fulltext %}
        <a title="fulltext" href="{{ site.url }}/pdf/{{ article.fulltext }}" target="_blank"><i class="fa fa-file-pdf-o"></i></a>
    {% endif %}
    <span class="title">{{ article.title }}</span>
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
        <a href="{{ article.URL }}" target="_blank">{{ article.URL }}</a>
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

{% assign start_2014_b = pub_base | minus: 1 %}
{% assign pub_base = pub_base | minus: site.data.pub-2014-b.size %}
<div class='panel-pub'>
<ol start='{{ start_2014_b }}' reversed>
{% for article in site.data.pub-2014-b %}
    <li>
    <div class="title">
    {% if article.fulltext %}
        <a title="fulltext" href="{{ site.url }}/pdf/{{ article.fulltext }}" target="_blank"><i class="fa fa-file-pdf-o"></i></a>
    {% endif %}
    <span class="title">{{ article.title }}</span>
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
        <a href="{{ article.URL }}" target="_blank">{{ article.URL }}</a>
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
