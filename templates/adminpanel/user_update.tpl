{% extends 'base.html' %}

{% block title %}{{ title }}{% endblock %}

{% block content %}
<h1>{{ title }}</h1>
<form method="post" enctype="multipart/form-data" class="col-md-6 col-lg-4 col-xl-3">
    {% csrf_token %}
    <div class="mb-3">
        <label for="id_username" class="form-label">Имя</label>
        <input type="text" class="form-control{% if register_form.username.errors %} is-invalid{% endif %}" name="username" id="id_username" {% if register_form.username.value %}value="{{ register_form.username.value }}"{% endif %}>
        {% for error in register_form.username.errors %}
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
<!--    <div class="mb-3">-->
<!--        <select class="form-select" aria-label="Default select example" name="group">-->
<!--            <option selected disabled>Группа допуска</option>-->
<!--            <option value="Users">Пользователь</option>-->
<!--            <option value="Stuff">Персонал</option>-->
<!--            <option value="Admins">Админ</option>-->
<!--        </select>-->
<!--    </div>-->
    <button type="submit" class="btn btn-primary">Создать</button>
</form>
{% endblock %}