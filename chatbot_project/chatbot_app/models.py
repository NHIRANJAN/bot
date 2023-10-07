from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class ChatbotResponse(models.Model):
    input_text = models.CharField(max_length=10000,null=True)
    response_text = models.CharField(max_length=10000,null=True)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.input_text

# chatbot_app/models.py
from django.db import models
from django.contrib.auth.models import User

class ChatHistory(models.Model):
    user_input = models.TextField(null=True)
    bot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"User Input: {self.user_input}, Timestamp: {self.timestamp}"
    
from django import forms

class EmailForm(forms.Form):
    user_email = forms.EmailField(label='User_email')
