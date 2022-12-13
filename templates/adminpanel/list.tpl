{% extends 'base.html' %}

{% block title %}{{ title }}{% endblock %}

{% block content %}
    <h1>Общая страница админки</h1>
    <ul>
        {% for link in admin_links %}
            {% for name in link.1 %}
                <li><a href='{{ name.0 }}/{{ link.0.1 }}'>{{ link.0.0 }}{{ name.1 }}</a></li>
            {% endfor %}
        {% endfor %}
    </ul>

    <h2>Полное содержимое сайта</h2>
    <ul>
        {% for link in admin_links_common %}
            <li><a href={{ link.0 }}>{{ link.1 }}</a></li>
        {% endfor %}
    </ul>
{% endblock %}