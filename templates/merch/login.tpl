{% extends 'base.html' %}

{% block title %}{{ title }}{% endblock %}

{% block content %}
<h1>
    Форма авторизации
</h1>
<form action="{% url 'merch:login' %}" method="post">
    {% csrf_token %}
    {{ login_form.as_p }}
    <br>
    <button type="submit">
        Войти
    </button>
</form>
<a href="{% url 'merch:register' %}" class="">
    Зарегистрироваться
</a>
{% endblock %}