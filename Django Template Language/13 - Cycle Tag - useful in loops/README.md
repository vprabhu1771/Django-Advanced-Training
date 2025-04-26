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