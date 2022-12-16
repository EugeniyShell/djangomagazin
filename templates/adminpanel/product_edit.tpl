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
        <label for="id_description" class="form-label">Описание (необязательное поле)</label>
        <textarea class="form-control{% if create_form.description.errors %} is-invalid{% endif %}" name="description" id="id_description" rows="1">{% comment %}
            {% endcomment %}{% if create_form.description.value %}{{ create_form.description.value }}{% endif %}{% comment %}
        {% endcomment %}</textarea>
        {% for error in create_form.description.errors %}
            <div class="invalid-feedback">{{ error }}</div>
        {% endfor %}
    </div>
    <div class="mb-3">
        <label for="id_description" class="form-label">Полное описание</label>
        <textarea class="form-control{% if create_form.description.errors %} is-invalid{% endif %}" name="short_desc" id="id_short_desc" rows="3">{% comment %}
            {% endcomment %}{% if create_form.short_desc.value %}{{ create_form.short_desc.value }}{% endif %}{% comment %}
        {% endcomment %}</textarea>
        {% for error in create_form.short_desc.errors %}
            <div class="invalid-feedback">{{ error }}</div>
        {% endfor %}
    </div>
    <div class="mb-3">
        <label for="id_description" class="form-label">Цена</label>
        <input type="number" class="form-control{% if create_form.description.errors %} is-invalid{% endif %}" name="price" id="id_price" {% if create_form.price.value %} value="{{ create_form.price.value }}"{% endif %}>
        {% for error in create_form.price.errors %}
            <div class="invalid-feedback">{{ error }}</div>
        {% endfor %}
    </div>
    <div class="mb-3">
        <label for="id_description" class="form-label">Количество на складе</label>
        <input type="number" class="form-control{% if create_form.description.errors %} is-invalid{% endif %}" name="quantity" id="id_quantity" {% if create_form.quantity.value %} value="{{ create_form.quantity.value }}"{% endif %}>
        {% for error in create_form.quantity.errors %}
            <div class="invalid-feedback">{{ error }}</div>
        {% endfor %}
    </div>
    <div class="mb-3">
        <select class="form-select{% if create_form.category.errors %} is-invalid{% endif %}" name="category" id="id_category">
            <option selected disabled>Выбор категории</option>
            {% for cat in catlist %}
                <option value="{{ cat.id }}">{{  cat.name  }}</option>
            {% endfor %}
        </select>
        {% for error in create_form.category.errors %}
            <div class="invalid-feedback">{{ error }}</div>
        {% endfor %}
    </div>
    <button type="submit" class="btn btn-primary">Сохранить</button>
</form>
{% endblock %}