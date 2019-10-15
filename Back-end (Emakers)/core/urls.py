from django.urls import path
from django.contrib.auth import views as v
from .views import (
    indexUser,
)

urlpatterns = [
    path('index', indexUser, name='index'),
    path('', v.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout', v.LogoutView.as_view(), name='logout'),
]