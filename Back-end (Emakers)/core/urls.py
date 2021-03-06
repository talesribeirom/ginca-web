from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index

# URLs das telas de login, logout e index
urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]