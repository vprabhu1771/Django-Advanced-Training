# https://www.youtube.com/watch?v=5xFzKklV_-M

Adjusting titles and labels in Django administration involves customizing how fields, models, and the overall admin interface are displayed. Here are several ways you can achieve this:

---

### 1. **Change the Admin Site Title**
You can change the title of the Django admin site using the `AdminSite` attributes.

**Example:**
Add this to your `admin.py`:
```python
from django.contrib import admin

admin.site.site_header = "My Custom Admin"
admin.site.site_title = "My Admin Portal"
admin.site.index_title = "Welcome to My Admin Portal"
```

---

### 2. **Customize Model Display Names**
You can set a user-friendly display name for models by defining the `verbose_name` and `verbose_name_plural` in your model.

**Example:**
```python
class Product(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Product Item"
        verbose_name_plural = "Product Items"
```

---

### 3. **Change Field Labels**
Use the `verbose_name` attribute for fields to provide a custom label in the admin interface.

**Example:**
```python
class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Product Name")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Product Price")
```

---

### 4. **Customize Field Display in the Admin**
You can adjust how fields are displayed in the admin by using the `ModelAdmin` class.

**Example:**
```python
from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('price',)
    search_fields = ('name',)

admin.site.register(Product, ProductAdmin)
```

---

### 5. **Change Labels for Actions**
If you need to rename default or custom actions in the admin, you can use the `short_description` attribute.

**Example:**
```python
class ProductAdmin(admin.ModelAdmin):
    actions = ['mark_as_featured']

    @admin.action(description='Mark selected products as featured')
    def mark_as_featured(self, request, queryset):
        queryset.update(is_featured=True)
```

---

### 6. **Customize Forms in Admin**
To provide finer control over field labels, you can customize the admin form.

**Example:**
```python
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'name': 'Product Name',
            'price': 'Product Price',
        }

class ProductAdmin(admin.ModelAdmin):
    form = ProductForm

admin.site.register(Product, ProductAdmin)
```

---

These changes will make your Django admin interface more user-friendly and tailored to your project needs. Let me know if you want help implementing any of these!