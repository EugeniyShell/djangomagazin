{% extends 'base.html' %}

{% block title %}{{ title }}{% endblock %}

{% block content %}
<h1>
    Изменить профиль
</h1>
<form action="{% url 'merch:register' %}" method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ edit_form.as_p }}
    <br>
    <button type="submit">
        Сохранить
    </button>
</form>
{% endblock %}