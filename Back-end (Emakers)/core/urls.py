from django.urls import path
from .views import (
    indexUser,
    novo_usuario,
)

urlpatterns = [
    path('', indexUser, name='index'),
    path('novo_usuario', novo_usuario, name='url_novo_usuario'),
]