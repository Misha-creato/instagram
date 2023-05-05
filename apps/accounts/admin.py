from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = (
        ('Information', {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active')
        }),
    )
    list_display = (
        'email', 
        'is_active', 
        'is_staff', 
        'is_superuser'
    )
    list_filter = (
        'email', 
        'is_active', 
        'date_joined'
    )
    readonly_fields = (
        'is_staff', 
        'is_superuser', 
        'date_joined'
    )
    ordering = (
        'email',
    )
    search_fields = (
        'email',
    )

admin.site.register(CustomUser, CustomUserAdmin)