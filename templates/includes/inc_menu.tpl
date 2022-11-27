{% with pre=request.resolver_match %}
    <ul class="links-menu">
        {% for link in links_menu %}
            <li{% if link.href == pre.url_name or link.href == ''|add:pre.namespace|add:':'|add:pre.url_name %} class="active"{% endif %}>
                <a href="{% url link.href %}">{{ link.name }}</a>
            </li>
        {% endfor %}
        {% if user.is_authenticated %}
            <li{% if pre.namespace == 'merch' and pre.url_name == 'edit' %} class="active"{% endif %}>
                <a href="{% url 'merch:edit' %}">{{ user.username }}</a>
            </li>
            <li>
                <a href="{% url 'merch:logout' %}">выйти</a>
            </li>
        {% else %}
            <li{% if pre.namespace == 'merch' and pre.url_name == 'login' %} class="active"{% endif %}>
                <a href="{% url 'merch:login' %}">войти</a>
            </li>
            <li{% if pre.namespace == 'merch' and pre.url_name == 'register' %} class="active"{% endif %}>
                <a href="{% url 'merch:register' %}">зарегистрироваться</a>
            </li>
        {% endif %}
    </ul>
    <a href="#" class="search"></a>
    <a href="{% url 'basket:view' %}" class="basket">
        <span>
            {% if basket %}
                В корзине: {{ basket|length }} предметов.
                {{ basket.0.total_cost|floatformat:0 }} руб
                ({{ basket.0.total_quantity }} шт)
            {% endif %}
        </span>
    </a>
{% endwith %}