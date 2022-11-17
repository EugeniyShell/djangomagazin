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
    <li>
        {% if user.is_authenticated %}
            {{ user.username }}
        {% else %}
            Вы не авторизованы!
        {% endif %}
    </li>
    <li>
        {% if user.is_authenticated %}
            <a href="{% url 'merch:logout' %}">выйти</a>
        {% else %}
            <a href="{% url 'merch:login' %}">войти</a>
        {% endif %}
    </li>
</ul>