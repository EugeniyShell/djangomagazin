<ul class="links-menu">
    {% for link in links_menu %}
        <li>
            {% with pre=request.resolver_match %}
                <a href="{% url link.href %}"
                    {% if link.href == pre.url_name or link.href == ''|add:pre.namespace|add:':'|add:pre.url_name %}class="active"{% endif %}
                >{{ link.name }}</a>
            {% endwith %}
        </li>
    {% endfor %}
    {% if user.is_authenticated %}
        <li>
            <a href="{% url 'merch:edit' %}">{{ user.username }}</a>
        </li>
        <li>
            <a href="{% url 'merch:logout' %}">выйти</a>
        </li>
    {% else %}
        <li>
            <a href="{% url 'merch:login' %}">войти</a>
        </li>
        <li>
            <a href="{% url 'merch:register' %}">зарегистрироваться</a>
        </li>
    {% endif %}
</ul>