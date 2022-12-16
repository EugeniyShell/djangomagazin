{% extends 'base.html' %}

{% block title %}Админка{% endblock %}

{% block content %}
    <h1>{{ title }}</h1>

    {% if primary_data %}
        <table class="table table-striped">
            <thead>
                <tr>
                    {% for key in primary_data.table %}
                        <th scope="col">{{ key }}</th>
                    {% endfor %}
                    <th scope="col"></th>
                    <th scope="col"></th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    {% for value in primary_data.table.values %}
                        <td>{{ value }}</td>
                    {% endfor %}
                    <td><a href="/ap/{{ primary_page }}/update/{{ primary_data.table.ID }}/">Редактировать</a></td>
                    <td><a href="/ap/{{ primary_page }}/delete/{{ primary_data.table.ID }}/">Удалить</a></td>
                </tr>
            </tbody>
        </table>
    {% endif %}

    {% if secondary_data %}
        <table class="table table-striped">
            <thead>
                <tr>
                    {% for key in secondary_data.0.table %}
                        <th scope="col">{{ key }}</th>
                    {% endfor %}
                    <th scope="col"></th>
                    <th scope="col"></th>
                </tr>
            </thead>
            <tbody>
                {% for item in secondary_data %}
                    <tr>
                        {% for value in item.table.values %}
                            <td>{{ value }}</td>
                        {% endfor %}
                        <td><a href="/ap/{{ secondary_page }}/update/{{ item.table.ID }}/">Редактировать</a></td>
                        <td><a href="/ap/{{ secondary_page }}/delete/{{ item.table.ID }}/">Удалить</a></td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    {% else %}
        <p>Пользователь не добавлял предметов в корзину.</p>
    {% endif %}

    <p><strong><a href="/ap/">В начало</a></strong></p>
{% endblock %}