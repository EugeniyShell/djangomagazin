{% extends 'base.html' %}

{% block title %}{{ title }}{% endblock %}

{% block content %}
    <h1>{{ product.name }}</h1>
    <p>
        {{ product.description }}
        <br>
        <a href="{% url 'basket:add' product.pk %}">КУПИТЬ</a>
    </p>
    <p>
        <a href="{% url 'products:category' product.category.pk %}">К странице категории</a>
        <br>
        {% if request.headers.referer %}
            <a href="{{ request.headers.referer }}">Назад</a>
        {% else %}
            <a href="javascript:history.back()">Назад</a>
        {% endif %}
    </p>
    {% if product.name == hot_product.name %}
        <p>Сегодня {{ product.name }} товар дня.</p>
    {% endif %}
{% endblock %}