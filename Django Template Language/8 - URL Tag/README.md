# 8 - URL Tag

# 1 - `views.py`
```python
from django.shortcuts import render

def about(request):
    return render(request, 'about.html')
```

# 2 - `urls.py`
```python
from django.urls import path
from frontend.views import about

urlpatterns = [
    path('about/', about, name='about'),
]
```

# 3 - `header.html`

**In another template**
```html
<a href="{% url 'about' %}">About Us</a>
```
