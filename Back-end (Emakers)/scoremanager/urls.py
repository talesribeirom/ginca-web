from django.urls import path
from .views import (
    list_events,
	apply_bonus,
	apply_penalty,
	list_ranking
)

# URLs de bonificação e penalidade, ranking e eventos
urlpatterns = [
    path('bonus/<int:id_user>/', apply_bonus, name='url_bonus'),
    path('penalty/<int:id_user>/',apply_penalty, name='url_penalty'),
    path('ranking/', list_ranking, name='url_ranking'),
    path('events/', list_events, name='url_events')
]