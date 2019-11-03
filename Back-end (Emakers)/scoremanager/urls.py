from django.urls import path
from .views import (
	create_score,
	score_detail,
	update_score,
	delete_score,
	apply_bonus,
	apply_penalty,
	apply_score,
	ranking
)


urlpatterns = [
    path('new_score/', create_score, name='url_new_score'),
    path('detail_score/<int:id_score>/', score_detail, name='url_detail_score'),
    path('change_score/<int:id_score>/', update_score, name='url_change_score'),
    path('remove_score/<int:id_score>/', delete_score, name='url_remove_score'),
    path('bonus/<int:id_user>/', apply_bonus, name='url_bonus'),
    path('penalty/<int:id_user>/',apply_penalty, name='url_penalty'),
    path('ponctuate/<int:id_user>/<slug:slug>/', apply_score, name='url_ponctuate'),
    path('ranking/', ranking, name='url_ranking')
]