from django.urls import path
from .views import (
	create_user,
	user_detail,
	update_user,
	delete_user,
	list_users
)


urlpatterns = [
    path('new_user/', create_user, name='url_new_user'),
    path('detail_user/<int:id_user>/', user_detail, name='url_detail_user'),
    path('change_user/<int:id_user>/', update_user, name='url_change_user'),
    path('remove_user/<int:id_user>/', delete_user, name='url_remove_user'),
	path('participants/', list_users, name='url_participants'),
]