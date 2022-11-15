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
</ul>