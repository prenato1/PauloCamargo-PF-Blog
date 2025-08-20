from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'sender', 'recipient', 'timestamp', 'is_read')
    list_filter = ('is_read', 'sender', 'recipient')
    search_fields = ('subject', 'body')
