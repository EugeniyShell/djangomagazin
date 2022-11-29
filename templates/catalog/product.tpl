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
        <br>
        <a href="{% url 'products:category' product.category.pk %}">Вернуться на обратно к списку товаров.</a>
    </p>
    {% if product.name == hot_product.name %}
        <p>Сегодня {{ product.name }} товар дня.</p>
    {% endif %}
{% endblock %}