### 5. **Includes**

# 1 - `views.py`

```python
from django.shortcuts import render

def home(request):
    return render(request, 'frontend/home.html')
```

# 2 - `urls.py`

```python
from django.urls import path

from frontend.views import home

urlpatterns = [
    path('', home, name='home')
]
```

# 3 - `home.html`

```html
<h1>Welcome</h1>

<!--Footer Partial-->
{% include 'frontend/layout/footer.html' %}
```

# 4 - `footer.html`

```html
<!-- Footer -->
<footer style="text-align: center; padding: 10px;">
    &copy; {% now "Y" %} My Website. All rights reserved.
</footer>
```

![Image](1.PNG)