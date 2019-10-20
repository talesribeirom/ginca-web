from django.urls import path
from .views import create_user


urlpatterns = [
    path('new_user/', create_user, name='url_new_user'),
]