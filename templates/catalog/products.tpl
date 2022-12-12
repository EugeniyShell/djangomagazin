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
            <div class="gridrow row">
                {% for item in prolist %}
                    <div class="col-sm-6 col-md-4 col-lg-3 col-xxl-2">
                        <div class="card">
                            <div class="card-header text-end">
                                {{ item.category }}
                            </div>
                            <div class="card-body">
                                <h5 class="card-title">{{ item.name }}</h5>
                                <p class="card-text">{{ item.description }}</p>
                                <a class="card-link" href="{% url 'products:product' item.category.pk item.pk %}">На страницу товара</a>
                                <br>
                                <a class="btn btn-primary" href="{% url 'basket:add' item.pk %}">КУПИТЬ</a>
                            </div>
                        </div>
                    </div>
                {% endfor %}
            </div>
        {% else %}
            <p>В этой категории товаров нет.</p>
        {% endif %}
        <p class="block">
            Товар дня: {{ hot_product.name }}.
        </p>
    {% endif %}
{% endblock %}