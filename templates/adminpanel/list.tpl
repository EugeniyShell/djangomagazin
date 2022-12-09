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
                </tr>
            </thead>
            <tbody>
                {% for item in item_list %}
                    <tr>
                        {% for value in item.table.values %}
                            <td>{{ value }}</td>
                        {% endfor %}
                    </tr>
                {% endfor %}
            </tbody>
            <tfoot>
                <tr>
                    <th scope="col" colspan="5"><a href='create/'>{{ title_name }}</a></th>
                </tr>
            </tfoot>
        </table>
    {% else %}
        <p>В корзине пусто.</p>
    {% endif %}
{% endblock %}