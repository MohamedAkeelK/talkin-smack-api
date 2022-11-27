from django.contrib import admin
from .models import Smack


@admin.register(Smack)
class SmackAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
