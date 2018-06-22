from django.urls import path,include
from . import views
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup_page'),
    path('logout/', views.LogOutView.as_view(), name='log_out')
]