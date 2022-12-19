{% with pre=request.resolver_match %}
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Переключатель навигации">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto links-menu">
                {% for link in links_menu %}
                    <li class="nav-item me-lg-4">
                        <a class="nav-link{% if link.href == pre.url_name or link.href == ''|add:pre.namespace|add:':'|add:pre.url_name %} active{% endif %}" aria-current="page" href="{% url link.href %}">{{ link.name }}</a>
                    </li>
                {% endfor %}
                {% if user.is_authenticated %}
                    <li class="nav-item me-lg-4">
                        <a class="nav-link{% if pre.namespace == 'merch' and pre.url_name == 'edit' %} active{% endif %}" href="{% url 'merch:edit' %}">{{ user.username }}</a>
                    </li>
                    <li class="nav-item me-lg-4">
                        <a class="nav-link basket{% if pre.namespace == 'basket' and pre.url_name == 'view' %} active{% endif %}" href="{% url 'basket:view' %}">
                            {% if basket_items %}
                                В корзине: {{ basket_items|length }} предметов.
                            {% else %}
                                Корзина пуста
                            {% endif %}
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/ap/">админка</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'merch:logout' %}">выйти</a>
                    </li>
                {% else %}
                    <li class="nav-item me-lg-4">
                        <a class="nav-link{% if pre.namespace == 'merch' and pre.url_name == 'login' %} active{% endif %}" href="{% url 'merch:login' %}">войти</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link{% if pre.namespace == 'merch' and pre.url_name == 'register' %} active{% endif %}" href="{% url 'merch:register' %}">зарегистрироваться</a>
                    </li>
                {% endif %}
            </ul>
        </div>
    </nav>
{% endwith %}