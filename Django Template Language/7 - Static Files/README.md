### 7. **Static Files**


### ✅ 1. Check STATICFILES Settings in `settings.py`

Make sure you have these lines in your `settings.py`:

```python
STATIC_URL = '/static/'

# During development
STATICFILES_DIRS = [BASE_DIR / "static"]

# During production (if collecting static files)
STATIC_ROOT = BASE_DIR / "staticfiles"
```


### ✅ Your Folder Structure Should Be:

```
your_project/
│
├── static/
│   └── images/
│       └── logo.png
```

And you should not put the `static` folder inside an app unless you configure it accordingly.

# 2 - `views.py`

```python
from django.shortcuts import render

def home(request):
    return render(request, 'frontend/home.html')
```

# 3 - `urls.py`

```python
from django.urls import path

from frontend.views import home

urlpatterns = [
    path('', home, name='home')
]
```

# 4 - `home.html` **In template:**

Use `{% load static %}` at the top of your HTML template

Your template should look like:

```html
{% load static %}

<img src="{% static 'images/logo.png' %}" alt="Logo">
```

### ✅ 4. During Development, `runserver` Must Serve Static Files

Make sure you are using `python manage.py runserver` and not some other web server during development.

---

### ✅ 5. Clear Browser Cache

Sometimes, the browser caches the 404 result. Try hard refreshing the page (Ctrl+F5).

---

If you've checked everything above and it's still not working, could you share:

1. Your folder structure for `static/images/logo.png`
2. Your `settings.py` `STATIC*` configuration

![Image](1.PNG)