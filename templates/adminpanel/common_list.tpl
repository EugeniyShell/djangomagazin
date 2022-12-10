{% extends 'base.html' %}

{% block title %}Админка{% endblock %}

{% block content %}
    <h1>{{ title }}</h1>

    {% if item_list %}
        <table class="table table-striped">
            <thead>
                <tr>
                    {% for key in item_list.0.table %}
                        <th scope="col">{{ key }}</th>
                    {% endfor %}
                    <th scope="col"></th>
                    <th scope="col"></th>
                </tr>
            </thead>
            <tbody>
                {% for item in item_list %}
                    <tr>
                        {% for value in item.table.values %}
                            <td>{{ value }}</td>
                        {% endfor %}
                        <td><a href="read/{{ item.table.ID }}/">Смотреть</a></td>
                        <td><a href="delete/{{ item.table.ID }}/">Удалить</a></td>
                    </tr>
                {% endfor %}
            </tbody>
            <tfoot>
                <tr>
                    <th scope="col" colspan="{{ item_list.0.table|length|add:'2' }}"><a href="create/">{{ title_name }}</a></th>
                </tr>
                <tr>
                    <th scope="col" colspan="{{ item_list.0.table|length|add:'2' }}"><a href="/ap/">В начало</a></th>
                </tr>
            </tfoot>
        </table>
    {% else %}
        <p>Тут ничего нет.</p>
    {% endif %}
{% endblock %}