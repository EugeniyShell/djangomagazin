{% extends 'base.html' %}

{% block title %}Продукты{% endblock %}

{% block content %}
<h1>Категории</h1>
<ul>
{% for item in categories %}
<li>{{ item.name }}</li>
{% endfor %}
</ul>

<h2>Продукты</h2>
<ul>
{% for item in products %}
<li>{{ item.name }}, {{ item.name }}</li>
{% endfor %}
</ul>
{% endblock %}
