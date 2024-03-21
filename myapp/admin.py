from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Message

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'image')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Message)
