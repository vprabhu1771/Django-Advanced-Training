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