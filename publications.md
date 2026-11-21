---
layout: page
title: Publications
title_zh: 论文
permalink: /publications/
last_updated: 2026-11-10
---
{% include pdf-icon.html %}
<p class="publication-updated"><span class="language-pair"><span class="en-only" lang="en">Last updated:</span><span class="zh-only" lang="zh-CN">最后更新：</span></span> <time datetime="{{ page.last_updated | date: '%Y-%m-%d' }}">{{ page.last_updated | date: '%B %-d, %Y' }}</time></p>

\|[**Google Scholar**](https://goo.gl/AgbNaK){:target="_blank" rel="noopener noreferrer"}
\|[**ResearchGate**](https://www.researchgate.net/profile/Tao_Cheng13){:target="_blank" rel="noopener noreferrer"}
\|[**ORCID**](http://orcid.org/0000-0003-4830-177X){:target="_blank" rel="noopener noreferrer"}
\|[**Web of Science**](https://www.webofscience.com/wos/author/record/1444044){:target="_blank" rel="noopener noreferrer"} \|  
|<span class="language-pair"><span class="en-only" lang="en">(citation:22,713; h-index:76; i10-index: 201 updated by April 4 2026)</span><span class="zh-only" lang="zh-CN">（引用：22,713；h指数：76；i10指数：201，更新于2026年4月4日）</span></span>
|  
{% if jekyll.environment == 'production' %}{% assign local = false %}{% else %}{% assign local = true %}{% endif %}
|[**26{% if local %}-28{% endif %}**](#2026)
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
<span class="language-pair"><span class="en-only" lang="en">Please send an email to [tcheng@suda.edu.cn](mailto:tcheng@suda.edu.cn), if full text is needed.</span><span class="zh-only" lang="zh-CN">如需全文，请发邮件至 [tcheng@suda.edu.cn](mailto:tcheng@suda.edu.cn)。</span></span>

## <a name="Selected"></a><span class="language-pair"><span class="en-only" lang="en">Selected</span><span class="zh-only" lang="zh-CN">代表性论文</span></span>
<div class='panel-pub'>
<ol start='10' reversed>
{% for article in site.data.representative %}
{% include publication-item.html %}
{% endfor %}
</ol>
</div>
<a href="#top"><span class="language-pair"><span class="en-only" lang="en">Back to top</span><span class="zh-only" lang="zh-CN">返回顶部</span></span></a>

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

## <a name="{{ year }}"></a>{% if year == '2014-b' %}<span class="language-pair"><span class="en-only" lang="en">before 2014</span><span class="zh-only" lang="zh-CN">2014年以前</span></span>{% else %}{{ year }}{% endif %}

<div class='panel-pub'>
<ol start='{{ pub_base }}' reversed>
{% for article in site.data[data_key] %}
{% include publication-item.html %}
{% endfor %}
</ol>
</div>
<a href="#top"><span class="language-pair"><span class="en-only" lang="en">Back to top</span><span class="zh-only" lang="zh-CN">返回顶部</span></span></a>
{% assign pub_base = pub_base | minus: site.data[data_key].size %}
{% endfor %}
