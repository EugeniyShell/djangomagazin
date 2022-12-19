{% extends 'base.html' %}

{% block title %}{{ title }}{% endblock %}

{% block content %}
    <h1>
        {{ title }}
    </h1>
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
            </tr>
        </tbody>
    </table>
    <br>
    <form href="/ap/products_list">
        <button type="submit" class="btn btn-primary">Подтвердить удаление</button>
    </form>
{% endblock %}