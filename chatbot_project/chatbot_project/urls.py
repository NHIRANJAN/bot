# your_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chatbot_app.urls')),  # Include your chatbot app's URLs
      # Include auth-related URLs
    # Other URL patterns
]
