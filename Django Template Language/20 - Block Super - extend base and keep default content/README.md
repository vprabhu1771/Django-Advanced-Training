### 20. **Block Super (extend base and keep default content)**
**base.html**
```html
{% block title %}Default Title{% endblock %}
```

**child.html**
```html
{% extends 'base.html' %}
{% block title %}My Page – {{ block.super }}{% endblock %}
```