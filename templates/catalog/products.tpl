{% extends 'base.html' %}

{% block title %}{{ title }}{% endblock %}

{% block content %}
    <h1>Категории товаров</h1>
    <ul>
        {% for item in catlist %}
            <li
                {% if item.name == catname %}
                    class="active"
                {% endif %}
            >
                <a href="{% url 'products:category' item.pk %}">
                    {{ item.name }}
                </a>
            </li>
        {% endfor %}
    </ul>
    {% if title %}
        <h2>{{ title }}</h2>
        {% if prolist %}
            <ul>
                {% for item in prolist %}
                    <li>
                        <b>{{ item.name }}</b>
                        <br>
                        {{ item.description }}
                        <br>
                        <a href="{% url 'basket:add' item.pk %}">КУПИТЬ</a>
                    </li>
                {% endfor %}
            </ul>
        {% else %}
            <p>В этой категории товаров нет.</p>
        {% endif %}
        <p class="block">
            Товар дня: {{ hot_product.name }}.
        </p>
    {% endif %}
{% endblock %}