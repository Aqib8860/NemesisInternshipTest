from django.urls import path
from core.views import *


app_name = 'core'

urlpatterns = [
    path('', LoginView.as_view(), name='user-login'),
    path('login', LoginView.as_view(), name='user-login'),
    path('home', HomeView.as_view(), name='home'),
    path('user-logout/', UserLogout, name='user-logout'),
    path('user-register/', UserRegistrationView.as_view(), name='user-register'),
    path('user-update/<str:user_id>', UpdateUserView.as_view(), name='user-update'),
    path('user-delete/<str:user_id>', DeleteUserView.as_view(), name='user-delete'),
]
