from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('wordcount/', wordcount, name='wordcount'),
    path('delete/', clear_memory, name='clear_memory'),
]
