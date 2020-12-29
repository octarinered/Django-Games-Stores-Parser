from django.contrib import admin
from django.urls import path, include, re_path
from djangoparser import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('parser_app.urls')),
]
