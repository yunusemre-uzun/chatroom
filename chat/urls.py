from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from chat import views


app_name = 'chat'
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup_page'),
    path('', views.UsernameView.as_view(), name = 'username'),
    path('<str:username>/chat/<str:receiver>' , views.ChatView.as_view(), name = 'chat_screen'),
    path('<str:username>/friends/',views.FriendView.as_view(),name='friend'),

]
