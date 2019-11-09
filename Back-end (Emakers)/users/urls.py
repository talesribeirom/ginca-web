from django.urls import path
from .views import (
	profile_user,
	list_users
)

# URLs para a tela de participantes e para o perfil
urlpatterns = [
	path('participants/', list_users, name='url_participants'),
	path('my_profile/', profile_user, name='url_my_profile')
]