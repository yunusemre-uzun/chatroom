from django.contrib import admin
from django.urls import path, re_path

from chat import views

app_name = 'chat'
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup_page'),
    path('', views.UsernameView.as_view(), name = 'username'),
    path('<str:username>/chat/<str:receiver>' , views.ChatView.as_view(), name = 'chat_screen'),
]
