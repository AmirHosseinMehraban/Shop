from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import MyUser
from django.contrib.auth.models import Group


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ['full_name', 'is_admin']
    list_filter = ['is_admin']
    fieldsets = [
        (None, {"fields": ['phone_number', 'password']}),
        ("Personal info", {'fields': ['full_name', 'email']}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["phone_number", "email", "fullname", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email", "phone_number"]
    ordering = ["full_name"]
    filter_horizontal = []


admin.site.register(MyUser, UserAdmin)

admin.site.unregister(Group)
