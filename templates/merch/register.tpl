{% extends 'base.html' %}

{% block title %}{{ title }}{% endblock %}

{% block content %}
<h1>
    Форма регистрации
</h1>
<form method="post" enctype="multipart/form-data" class="col-md-6 col-lg-4 col-xl-3">
    {% csrf_token %}
    <div class="mb-3">
        <label for="id_username" class="form-label">Ваше имя</label>
        <input type="text" class="form-control{% if register_form.username.errors %} is-invalid{% endif %}" name="username" id="id_username" {% if register_form.username.value %}value="{{ register_form.username.value }}"{% endif %}>
        {% for error in register_form.username.errors %}
            <div class="invalid-feedback">{{ error }}</div>
        {% endfor %}
    </div>
    <div class="mb-3">
        <label for="id_password1" class="form-label">Пароль</label>
        <input type="password" class="form-control{% if register_form.password1.errors %} is-invalid{% endif %}" name="password1" id="id_password1" {% if register_form.password1.value %}value="{{ register_form.password1.value }}"{% endif %}>
        {% for error in register_form.password1.errors %}
            <div class="invalid-feedback">{{ error }}</div>
        {% endfor %}
    </div>
    <div class="mb-3">
        <label for="id_password2" class="form-label">Повтор пароля</label>
        <input type="password" class="form-control{% if register_form.password2.errors %} is-invalid{% endif %}" name="password2" id="id_password2" {% if register_form.password2.value %}value="{{ register_form.password2.value }}"{% endif %}>
        {% for error in register_form.password2.errors %}
            <div class="invalid-feedback">{{ error }}</div>
        {% endfor %}
    </div>
    <div class="mb-3">
        <label for="id_email" class="form-label">Почта</label>
        <input type="email" class="form-control{% if register_form.email.errors %} is-invalid{% endif %}" name="email" id="id_email" {% if register_form.email.value %}value="{{ register_form.email.value }}"{% endif %}>
        {% for error in register_form.email.errors %}
            <div class="invalid-feedback">{{ error }}</div>
        {% endfor %}
    </div>
    <button type="submit" class="btn btn-primary">Зарегистрироваться</button>
</form>
{% endblock %}