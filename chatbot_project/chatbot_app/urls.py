# chatbot_app/urls.py

from django.urls import path
from . import views
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.chatbot, name='chatbot'),
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
    path('test/', views.test_page, name='test_page'),
        # path('chat_history/', views.chat_history, name='chat_history'),
]
