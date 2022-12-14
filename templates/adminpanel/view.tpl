{% extends 'base.html' %}

{% block title %}Админка{% endblock %}

{% block content %}
    <h1>{{ title }}</h1>

    {% if item_list %}
        <table class="table table-striped">
            <thead>
                <tr>
                    {% for key in item_list.table %}
                        <th scope="col">{{ key }}</th>
                    {% endfor %}
                    <th scope="col"></th>
                    <th scope="col"></th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    {% for value in item_list.table.values %}
                        <td>{{ value }}</td>
                    {% endfor %}
                    <td><a href="/ap/{{ page }}/edit/{{item_list.table.ID}}/">Редактировать</a></td>
                    <td><a href="/ap/{{ page }}/delete/{{item_list.table.ID}}/">Удалить</a></td>
                </tr>
            </tbody>
        </table>
    {% endif %}

    {% if basket_items %}
        <table class="table table-striped">
            <thead>
                <tr>
                    {% for key in basket_items.0.table %}
                        <th scope="col">{{ key }}</th>
                    {% endfor %}
                    <th scope="col"></th>
                    <th scope="col"></th>
                </tr>
            </thead>
            <tbody>
                {% for item in basket_items %}
                    <tr>
                        {% for value in item.table.values %}
                            <td>{{ value }}</td>
                        {% endfor %}
                        <td><a href="/ap/{{ page }}/edit/{{item_list.table.ID}}/">Редактировать</a></td>
                        <td><a href="/ap/{{ page }}/delete/{{item_list.table.ID}}/">Удалить</a></td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    {% else %}
        <p>Пользователь не добавлял предметов в корзину.</p>
    {% endif %}

    <p><strong><a href="/ap/">В начало</a></th></strong></p>
{% endblock %}