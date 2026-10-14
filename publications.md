---
layout: page
title: Publications
permalink: /publications/
last_updated: 2026-10-14
---
<p class="publication-updated">Last updated: <time datetime="{{ page.last_updated | date: '%Y-%m-%d' }}">{{ page.last_updated | date: '%B %-d, %Y' }}</time></p>

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
{% include publication-item.html %}
{% endfor %}
</ol>
</div>
<a href="#top">Back to top</a>

{% assign pub_years = "2026,2025,2024,2023,2022,2021,2020,2019,2018,2017,2016,2015,2014,2014-b" | split: "," %}
{% comment %}Count all papers, then decrease the reversed list start for each year.
New papers automatically receive the next highest number.{% endcomment %}
{% assign pub_base = 0 %}
{% for year in pub_years %}
{% assign data_key = "pub-" | append: year %}
{% assign pub_base = pub_base | plus: site.data[data_key].size %}
{% endfor %}
{% for year in pub_years %}
{% assign data_key = "pub-" | append: year %}

## <a name="{{ year }}"></a>{% if year == '2014-b' %}before 2014{% else %}{{ year }}{% endif %}

<div class='panel-pub'>
<ol start='{{ pub_base }}' reversed>
{% for article in site.data[data_key] %}
{% include publication-item.html %}
{% endfor %}
</ol>
</div>
<a href="#top">Back to top</a>
{% assign pub_base = pub_base | minus: site.data[data_key].size %}
{% endfor %}
