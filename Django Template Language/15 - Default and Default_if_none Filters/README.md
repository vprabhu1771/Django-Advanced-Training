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