from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'username',
                    'is_staff', 'is_superuser',
                    'role', 'is_user_allow_to_dashboard']
    list_editable = ['is_user_allow_to_dashboard']
    list_filter = ['role']
    ordering = ['role']


admin.site.register(User, CustomUserAdmin)
