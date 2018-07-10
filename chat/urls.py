from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from chat import views


app_name = 'chat'
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup_page'),
    path('', views.UsernameView.as_view(), name = 'username'),
    path('<str:username>/chat/<str:receiver>/<str:message_text>/' , views.SaveMessageView.as_view(), name = 'chat_screen'),
    path('<str:username>/friends/',views.FriendView.as_view(),name='friends'),
    path('chatroom/<str:username>/', views.AjaxChatView.as_view(), name='ajax_chat'),
    path('ajaxFriends/<str:username>', views.FriendView2.as_view(), name='friend'),
    path('notification/<str:username>', views.NotificationView.as_view(), name='notification'),
    path('loadmore/<str:username>/<str:receiver>/',views.LoadMoreView.as_view(),name = 'load_more'),
]
