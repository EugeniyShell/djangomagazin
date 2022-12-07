{% extends 'base.html' %}

{% block title %}Корзина{% endblock %}

{% block content %}
    <h1>Корзина</h1>
    <p>Пользователь {{ user.username}}</p>
    {% if basket_items %}
        <table class="basket_list">
            <tr>
                <th>Товар</th>
                <th>Цена</th>
                <th>Количество</th>
                <th>Сумма</th>
                <th>Удалить</th>
            </tr>
            {% for item in basket_items %}
                <tr>
                    <td>{{ item.product.name }}</td>
                    <td>{{ item.product.price }} руб</td>
                    <td><input type="number" name="{{ item.pk }}" min="0" value="{{ item.quantity }}"></td>
                    <td>{{ item.product_cost }}</td>
                    <td><a href="{% url 'basket:remove' item.pk %}" class="">&times;</a></td>
                </tr>
            {% endfor %}
            <tr>
                <th colspan="5">Итого: {{ basket_items.0.total_cost }} руб</th>
            </tr>
        </table>
    {% else %}
        <p>В корзине пусто.</p>
    {% endif %}
{% endblock %}
