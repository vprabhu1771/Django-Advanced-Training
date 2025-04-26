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