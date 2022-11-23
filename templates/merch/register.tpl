{% extends 'base.html' %}

{% block title %}{{ title }}{% endblock %}

{% block content %}
<h1>
    Форма регистрации
</h1>
<form action="{% url 'merch:register' %}" method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ register_form.as_p }}
    <br>
    <button type="submit">
        Зарегистрироваться
    </button>
</form>
{% endblock %}