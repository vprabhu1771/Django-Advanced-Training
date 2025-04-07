To generate a QR code in a Django project, you can use the `qrcode` Python library. Here's a simple step-by-step guide:

---

### ✅ Step 1: Install `qrcode` and `pillow`

```bash
pip install qrcode[pil]
```

---

### ✅ Step 2: Create a utility function for QR code generation

You can place this in a `utils.py` file or directly in a view:

```python
# utils.py or views.py
import qrcode
from io import BytesIO
from django.core.files import File
from django.core.files.base import ContentFile

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    buffer = BytesIO()
    img.save(buffer, format='PNG')
    return ContentFile(buffer.getvalue())
```

---

### ✅ Step 3: Create a Django view that returns the QR code image

```python
# views.py
from django.http import HttpResponse
from .utils import generate_qr_code

def qr_code_view(request):
    data = request.GET.get('data', 'https://example.com')  # or any default
    qr_image = generate_qr_code(data)
    return HttpResponse(qr_image, content_type='image/png')
```

---

### ✅ Step 4: Add URL pattern

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('qr/', views.qr_code_view, name='qr-code'),
]
```

---

### ✅ Step 5: Use it in a template

```html
<img src="{% url 'qr-code' %}?data=https://example.com" alt="QR Code" />
```

---

### ✅ Optional: Save QR Code in a Model (e.g., for a user or product)

```python
# models.py
from django.db import models
from .utils import generate_qr_code

class Product(models.Model):
    name = models.CharField(max_length=255)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        data = f"Product: {self.name}"
        qr_image = generate_qr_code(data)
        self.qr_code.save(f"{self.name}_qr.png", qr_image, save=False)
        super().save(*args, **kwargs)
```

---

Let me know if you'd like to generate QR codes with custom colors, logos, or for downloading as PDF!