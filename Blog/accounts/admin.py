from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'name', 'is_staff']

    # Define fieldsets without including usable_password
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('name',)}),
    )

    # Ensure usable_password is excluded if it's being referenced
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if 'usable_password' in form.base_fields:
            del form.base_fields['usable_password']
        return form


admin.site.register(CustomUser, CustomUserAdmin)
