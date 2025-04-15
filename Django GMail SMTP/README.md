To send emails using Gmail's SMTP server in Django, you can configure the `settings.py` file like this:.

```
pip install python-dotenv
```

### ✅ 1. Gmail SMTP Configuration in `settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'        # Your Gmail address
EMAIL_HOST_PASSWORD = 'your_app_password'       # Use App Password (not your Gmail password)
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
```

`.env`
```
EMAIL_HOST_USER=""
EMAIL_HOST_PASSWORD=""
```

### ✅ 2. Gmail SMTP Configuration in `settings.py`:

```python
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
```

---

### ✅ 2. Enable "App Password" in Gmail:
Google has disabled "Less Secure Apps" access. To use Gmail SMTP:

1. Go to [Google Account Security Settings](https://myaccount.google.com/security)
2. Enable **2-Step Verification** (if not already).
3. After that, go to [App Passwords](https://myaccount.google.com/apppasswords)
4. Generate a new **App Password** (select Mail > Other > Django)
5. Use that password in `EMAIL_HOST_PASSWORD`.

---

### ✅ 3. Sending an Email Example:

```python
from django.core.mail import send_mail

send_mail(
    subject='Hello from Django',
    message='This is a test email sent from Django using Gmail SMTP.',
    from_email='your_email@gmail.com',
    recipient_list=['recipient@example.com'],
    fail_silently=False,
)
```

---

### ✅ 4. Optional: Testing in Development
For development, you can use Django’s console backend to test emails:

```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

---

Let me know if you want to send HTML emails, attachments, or use `EmailMessage` or `EmailMultiAlternatives` for advanced use cases!