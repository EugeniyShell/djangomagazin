{% extends 'base.html' %}

{% block title %}{{ title }}{% endblock %}

{% block content %}
<h1>
    Форма авторизации
</h1>
<form action="{% url 'merch:login' %}" method="post" class="col-md-6 col-lg-4 col-xl-3">
    {% csrf_token %}
    {% if next %}
        <input type="hidden" name="next" value="{{ next }}">
    {% endif %}
    <div class="mb-3">
        <label for="id_username" class="form-label">Ваше имя</label>
        <input type="text" class="form-control{% if login_form.non_field_errors %} is-invalid{% endif %}" name="username" id="id_username">
    </div>
    <div class="mb-3">
        <label for="id_password" class="form-label">Пароль</label>
        <input type="password" class="form-control{% if login_form.non_field_errors %} is-invalid{% endif %}" name="password" id="id_password">
    </div>
    {% if login_form.non_field_errors %}
    <div class="mb-3">
        <div class="invalid-feedback nonfield">Пожалуйста, введите правильные имя пользователя и пароль. Оба поля могут быть чувствительны к регистру.</div>
    </div>
    {% endif %}
    <button type="submit" class="btn btn-primary">Войти</button>
</form>
<a href="{% url 'merch:register' %}" class="">
    Зарегистрироваться
</a>
{% endblock %}