### 10. **Custom Template Tag**
**myapp/templatetags/custom_tags.py**
```python
from django import template

register = template.Library()

@register.simple_tag
def multiply(x, y):
    return x * y
```

**template.html**
```html
{% load custom_tags %}
<p>{% multiply 4 5 %}</p>  <!-- Output: 20 -->
```