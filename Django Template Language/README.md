Here’s a list of **Django Template Language (DTL)** topics with examples, including corresponding `views.py` and `template.html` code:

---
### 3. **For Loop**
**views.py**
```python
def list_fruits(request):
    fruits = ['Apple', 'Banana', 'Cherry']
    return render(request, 'list_fruits.html', {'fruits': fruits})
```

**list_fruits.html**
```html
<ul>
  {% for row in fruits %}
    <li>{{ row }}</li>
  {% endfor %}
</ul>
```

---

### 4. **Filters**
**views.py**
```python
def show_user(request):
    return render(request, 'show_user.html', {'username': 'john doe'})
```

**show_user.html**
```html
<p>{{ username|title }}</p>  <!-- Output: John Doe -->
```

---

### 5. **Includes**
**views.py**
```python
def homepage(request):
    return render(request, 'home.html')
```

**home.html**
```html
<h1>Welcome</h1>
{% include 'footer.html' %}
```

**footer.html**
```html
<p>Copyright © 2025</p>
```

---

### 6. **Template Inheritance**
**base.html**
```html
<html>
  <body>
    <header>{% block header %}{% endblock %}</header>
    <main>{% block content %}{% endblock %}</main>
  </body>
</html>
```

**child.html**
```html
{% extends 'base.html' %}

{% block header %}
<h1>This is Header</h1>
{% endblock %}

{% block content %}
<p>This is the main content.</p>
{% endblock %}
```

**views.py**
```python
def page_view(request):
    return render(request, 'child.html')
```

---

### 7. **Static Files**
**settings.py**
```python
STATIC_URL = '/static/'
```

**In template:**
```html
{% load static %}
<img src="{% static 'images/logo.png' %}" alt="Logo">
```

---

### 8. **URL Tag**
**urls.py**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
]
```

**views.py**
```python
def about(request):
    return render(request, 'about.html')
```

**In another template**
```html
<a href="{% url 'about' %}">About Us</a>
```

---

Would you like me to provide more advanced examples like custom filters, tags, or context processors too?


Great! Let’s continue with **more advanced Django Template Language (DTL)** topics with examples and `views.py`:

---

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

---

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

---

### 11. **Using `with` Tag**
**views.py**
```python
def show_prices(request):
    return render(request, 'show_prices.html', {'price': 100, 'tax': 20})
```

**show_prices.html**
```html
{% with total=price|add:tax %}
  <p>Total Price: {{ total }}</p>
{% endwith %}
```

---

### 12. **Comment Tag**
```html
{% comment %}
This will not be rendered
{% endcomment %}
```

---

### 13. **Cycle Tag (useful in loops)**
**views.py**
```python
def show_items(request):
    items = ['One', 'Two', 'Three']
    return render(request, 'cycle.html', {'items': items})
```

**cycle.html**
```html
<ul>
  {% for item in items %}
    <li class="{% cycle 'odd' 'even' %}">{{ item }}</li>
  {% endfor %}
</ul>
```

---

### 14. **Now Tag (current date/time)**
```html
<p>Today is {% now "Y-m-d H:i" %}</p>
```

---

### 15. **Default and Default_if_none Filters**
**views.py**
```python
def profile(request):
    return render(request, 'profile.html', {'bio': None})
```

**profile.html**
```html
<p>{{ bio|default:"No bio available" }}</p>
<p>{{ bio|default_if_none:"No bio available" }}</p>
```

---

### 16. **Verbatim Tag (show code as-is)**
```html
{% verbatim %}
    {{ this will not be rendered }}
{% endverbatim %}
```

---

### 17. **Length and Length_is Filters**
**views.py**
```python
def fruit_count(request):
    fruits = ['Apple', 'Banana']
    return render(request, 'fruit_count.html', {'fruits': fruits})
```

**fruit_count.html**
```html
<p>Total: {{ fruits|length }}</p>
{% if fruits|length_is:2 %}
  <p>Exactly two fruits!</p>
{% endif %}
```

---

### 18. **Pluralize Filter**
**views.py**
```python
def cart(request):
    return render(request, 'cart.html', {'item_count': 1})
```

**cart.html**
```html
<p>You have {{ item_count }} item{{ item_count|pluralize }} in your cart.</p>
```

---

### 19. **`ifequal` and `ifnotequal` (older, mostly replaced by `if`)**
```html
{% ifequal user.role "admin" %}
    <p>You are an admin.</p>
{% endifequal %}
```

---

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

---

Would you like a downloadable cheat sheet or all of this as a single `.md` file?
