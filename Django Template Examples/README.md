Here’s a list of **Django Template Language (DTL)** topics with examples, including corresponding `views.py` and `template.html` code:

---

### 1. **Variable Rendering**
**views.py**
```python
from django.shortcuts import render

def show_name(request):
    return render(request, 'show_name.html', {'name': 'John'})
```

**show_name.html**
```html
<p>Hello, {{ name }}</p>
```

---

### 2. **If Condition**
**views.py**
```python
def check_user(request):
    return render(request, 'check_user.html', {'is_logged_in': True})
```

**check_user.html**
```html
{% if is_logged_in %}
    <p>Welcome back!</p>
{% else %}
    <p>Please login.</p>
{% endif %}
```

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
  {% for fruit in fruits %}
    <li>{{ fruit }}</li>
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