<ul class="links-menu">
    {% for link in links_menu %}
        <li>
            {% with pre=request.resolver_match %}
                <a class="{% if pre.url_name == link.href or pre.namespace|add:':'|add:pre.url_name == link.href %}
                    active
                {% endif %}" href="{% url link.href %}">
                    {{ link.name }}
                </a>
            {% endwith %}
        </li>
    {% endfor %}
</ul>