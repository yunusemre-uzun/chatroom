from django.contrib import admin
from django.urls import path, re_path

from chat import views

app_name = 'chat'
urlpatterns = [
    re_path(r'^$', views.UsernameView.as_view(), name = 'username'),
    path('<str:username>/chat/' , views.ChatView.as_view(), name = 'chat_screen')

]
