# sticky_notes/urls.py
from django.contrib import admin
from django.urls import path, include     # <-- IMPORT include (not a class)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notes.urls')),      # include notes app urls at the root
]