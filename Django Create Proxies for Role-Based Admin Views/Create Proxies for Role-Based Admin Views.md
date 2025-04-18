You're trying to register **different Django admin views** for the same `CustomUser` model based on **user roles** like **Author**, **Member**, and **Admin**, which are likely **user groups** or roles stored in a `CustomUser` field or `Group`.

Since Django doesn't allow registering the **same model twice** using `@admin.register()`, you'll need to customize the admin to **filter users by group or role**, and display them separately in different admin views.

---

### ✅ Recommended Solution: Create Proxies for Role-Based Admin Views

You can use **proxy models** to register the same `CustomUser` model multiple times but with different filters for each role.

---

### 🧩 Step-by-Step Implementation

#### 1. Add Proxy Models in `models.py`

```python
class AuthorUser(CustomUser):
    class Meta:
        proxy = True
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class MemberUser(CustomUser):
    class Meta:
        proxy = True
        verbose_name = 'Member'
        verbose_name_plural = 'Members'


class AdminUser(CustomUser):
    class Meta:
        proxy = True
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'
```

---

#### 2. Create Custom Admins in `admin.py`

```python
from django.contrib import admin
from django.utils.html import format_html
from .models import CustomUser, AuthorUser, MemberUser, AdminUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin

class BaseCustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('email', 'gender', 'image_tag', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    search_fields = ('email',)
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'gender', 'password', 'groups')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'gender', 'password1', 'password2', 'is_staff', 'is_active', 'groups')}
         ),
    )

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Image'

# Filter users by group or role (adjust logic if using roles instead of groups)
@admin.register(AuthorUser)
class AuthorAdmin(BaseCustomUserAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(groups__name='Author')


@admin.register(MemberUser)
class MemberAdmin(BaseCustomUserAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(groups__name='Member')


@admin.register(AdminUser)
class AdminUserAdmin(BaseCustomUserAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(groups__name='Admin')
```

---

### ✅ Now in the Django Admin Panel:
- You will see **Authors**, **Members**, and **Admins** as separate sections.
- Each will list only the users in their respective group.

---

Let me know if you're using a different way to assign roles (e.g., a `role` field instead of Django groups), and I’ll tweak the code for that!