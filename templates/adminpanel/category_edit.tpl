{% extends 'base.html' %}

{% block title %}{{ title }}{% endblock %}

{% block content %}
<h1>{{ title }}</h1>
<form method="post" enctype="multipart/form-data" class="col-md-6 col-lg-4 col-xl-3">
    {% csrf_token %}
    <div class="mb-3">
        <label for="id_name" class="form-label">Название</label>
        <input type="text" class="form-control{% if create_form.name.errors %} is-invalid{% endif %}" name="name" id="id_name" {% if create_form.name.value %}value="{{ create_form.name.value }}"{% endif %}>
        {% for error in create_form.name.errors %}
            <div class="invalid-feedback">{{ error }}</div>
        {% endfor %}
    </div>
    <div class="mb-3">
        <label for="id_description" class="form-label">Описание</label>
        <textarea class="form-control{% if create_form.description.errors %} is-invalid{% endif %}" name="description" id="id_description" rows="3">{% comment %}
            {% endcomment %}{% if create_form.description.value %}{{ create_form.description.value }}{% endif %}{% comment %}
        {% endcomment %}</textarea>
        {% for error in create_form.description.errors %}
            <div class="invalid-feedback">{{ error }}</div>
        {% endfor %}
    </div>
    <button type="submit" class="btn btn-primary">Сохранить</button>
</form>
{% endblock %}