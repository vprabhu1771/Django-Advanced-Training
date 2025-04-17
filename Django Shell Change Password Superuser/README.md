Ah, you're trying to create a superuser with email and password directly like this:

```bash
python manage.py createsuperuser admin@gmail.com admin admin
```

But that won't work unless you've **customized your User model** to accept email as the username, and even then, the `createsuperuser` command doesn’t accept arguments that way by default.

---

### ✅ Here's how to properly create a superuser

#### Option 1: **Interactive mode (default, safe)**

Just run:

```bash
python manage.py createsuperuser
```

Then follow the prompts:

```plaintext
Username: admin
Email address: admin@gmail.com
Password: ********
Password (again): ********
```

---

### ✅ Option 2: **Using arguments (only works with custom user model + custom manager)**
If you’re using a **custom user model** where `USERNAME_FIELD = 'email'`, you can use:

```bash
python manage.py createsuperuser --email admin@gmail.com --password admin
```

BUT: Django **does not allow setting password via command line** for security. So this will still fail unless you write a custom management command.

---

### ✅ Bonus: Fix "Please enter the correct username and password" error

That message appears **after login**, not during creation. Here's why it might happen:

1. You created the user but typed the wrong password at login.
2. You’re trying to log in with email, but Django expects username (unless customized).
3. You didn’t set `is_staff = True` or `is_superuser = True`.

---

### ✅ Verify user in Django shell:

```bash
python manage.py shell
```

```python
from django.contrib.auth import get_user_model
User = get_user_model()

user = User.objects.get(username='admin')  # or email='admin@gmail.com' if customized
print(user.is_staff, user.is_superuser)
```

If they’re not `True`, set them:

```python
user.is_staff = True
user.is_superuser = True
user.set_password('admin')  # to reset password
user.save()
```

---

Let me know if you’re using a **custom user model** with `email` login — I can guide you on that too!


# OR


### ✅ Step-by-Step Checklist

#### ✅ 1. Confirm user exists and is a staff/superuser

Run:

```bash
python manage.py shell
```

Then:

```python
from django.contrib.auth import get_user_model
User = get_user_model()

# Check the user (use correct username/email based on your model)
user = User.objects.get(username='admin')  # or email='admin@gmail.com' if using custom user model

print(user.is_active, user.is_staff, user.is_superuser)
```

Expected output:

```python
(True, True, True)
```

If any of them are False:

```python
user.is_staff = True
user.is_superuser = True
user.is_active = True
user.set_password('admin')  # reset password
user.save()
```

---

#### ✅ 2. Check if you're using **custom user model** with email as username

If you created a custom user model and changed this:

```python
USERNAME_FIELD = 'email'
```

Then at login, you should be entering the **email**, not username.

Make sure your login form and `UserAdmin` are configured for it.

---

#### ✅ 3. Confirm password is set correctly

In the shell:

```python
user.check_password('admin')  # returns True or False
```

If `False`, run:

```python
user.set_password('admin')
user.save()
```

---

#### ✅ 4. Try to create a new superuser (interactively)

Just to confirm it works:

```bash
python manage.py createsuperuser
```

Enter:
- username: `testadmin`
- email: `test@example.com`
- password: `test1234`

Then log in using those exact credentials.

---

### 🧪 Still not working?

Please tell me:

1. Are you using a custom user model?
2. What exactly are you typing into the login fields?
3. What authentication backend is configured (`settings.py`)?

I'll help you fix it right away.
