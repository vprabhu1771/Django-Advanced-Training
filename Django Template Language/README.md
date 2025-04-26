Here’s a list of **Django Template Language (DTL)** topics with examples, including corresponding `views.py` and `template.html` code:


Would you like me to provide more advanced examples like custom filters, tags, or context processors too?


Great! Let’s continue with **more advanced Django Template Language (DTL)** topics with examples and `views.py`:


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
