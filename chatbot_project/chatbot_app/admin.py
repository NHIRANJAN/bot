from django.contrib import admin
from .models import ChatbotResponse
from .models import ChatHistory
class ChatbotResponseAdmin(admin.ModelAdmin):
    list_display = ('input_text', 'response_text', 'created_at')  # Add 'created_at' to the list display
class chatHistoryAdmin(admin.ModelAdmin):
    list_display=('user_input','bot_response','timestamp')
admin.site.register(ChatHistory,chatHistoryAdmin)
admin.site.register(ChatbotResponse, ChatbotResponseAdmin)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
