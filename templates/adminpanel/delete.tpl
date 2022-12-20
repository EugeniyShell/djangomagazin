{% extends 'base.html' %}

{% block title %}{{ title }}{% endblock %}

{% block content %}
    <h1>
        {{ title }}
    </h1>
    {% if title2 %}
            {{ title2 }}
    {% endif %}
    <table class="table table-striped">
        <thead>
            <tr>
                {% for key in primary_data.table %}
                    <th scope="col">{{ key }}</th>
                {% endfor %}
            </tr>
        </thead>
        <tbody>
            <tr>
                {% for value in primary_data.table.values %}
                    <td>{{ value }}</td>
                {% endfor %}
            </tr>
        </tbody>
    </table>
    <br>
    <form method="POST">
        {% csrf_token %}
        <button type="submit" class="btn btn-danger">Подтвердить удаление</button>
        <a href="javascript:history.back()" class="btn btn-primary">Не удалять</a>
    </form>
{% endblock %}