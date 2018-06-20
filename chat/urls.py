from django.contrib import admin
from django.urls import path, re_path

from chat import views

app_name = 'chat'
urlpatterns = [
    re_path(r'^$', views.ChatView.as_view(), name = 'chat_screen'),
]
