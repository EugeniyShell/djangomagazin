{% extends 'base.html' %}

{% block title %}Продукты{% endblock %}

{% block content %}
    <h1>{{ title }}</h1>
    <ul>
        {% for item in list %}
            <li>
                <a href="{% url 'products:category' item.pk %}">
                    {{ item.name }}
                </a>
            </li>
        {% endfor %}
    </ul>
{% endblock %}
