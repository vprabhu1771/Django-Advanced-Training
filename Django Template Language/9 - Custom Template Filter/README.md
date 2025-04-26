### 9. **Custom Template Filter**
Create a file called `templatetags/custom_filters.py` inside your app.

**myapp/templatetags/custom_filters.py**
```python
from django import template

register = template.Library()

@register.filter
def upper_case(value):
    return value.upper()
```

**Enable the filter in your template**

**template.html**
```html
{% load custom_filters %}
<p>{{ "hello world"|upper_case }}</p>  <!-- Output: HELLO WORLD -->
```