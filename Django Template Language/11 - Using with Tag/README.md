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