from django.shortcuts import render
from django.shortcuts import (
	render,
	redirect
)
from django.http import HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from .forms import (
	Score_Form,
	Apply_Score_Form
)
from .models import (
	Score,
	User,
	User_has_score
)
from operator import itemgetter
import json

def get_ranking():
	users = User.objects.all()
	total_score_users = {}
	for user in users:
		sum_score_user = 0
		for user_has_score in user.user_has_scores.all():
			sum_score_user += user_has_score.score.equivalent_score
		total_score_users[user.username] = sum_score_user

	ranking = sorted(total_score_users.items(), key=itemgetter(1), reverse=True)

	return ranking;

@login_required
def list_ranking(request):
	ranking = get_ranking()
	return render(request, 'ranking.html', {'ranking': ranking})

@login_required
def apply_bonus(request, id_user):
	if request.user.is_superuser:
		userAux = User.objects.get(pk=id_user)
		form = Apply_Score_Form(request.POST)
		scores = Score.objects.filter(score_specification='B')

		if request.POST:
			mutable = request.POST._mutable
			request.POST._mutable = True
			score_data = json.loads(form.data['score'])
			form.data['score'] = score_data['score_id']
			request.POST._mutable = mutable

		if form.is_valid():
			form.save()
			return redirect('url_participants')

		return render(request, 'apply-bonus.html', {'form': form, 'userAux': userAux, 'scores': scores})
	else:
		return HttpResponseNotFound()

@login_required
def apply_penalty(request, id_user):
    if request.user.is_superuser:
        userAux = User.objects.get(pk=id_user)
        form = Apply_Score_Form(request.POST)
        scores = Score.objects.filter(score_specification='P')

        if request.POST:
            mutable = request.POST._mutable
            request.POST._mutable = True
            score_data = json.loads(form.data['score'])
            form.data['score'] = score_data['score_id']
            request.POST._mutable = mutable

        if form.is_valid():
            form.save()
            return redirect('url_participants')

        return render(request, 'apply-penalty.html', {'form': form, 'userAux': userAux, 'scores': scores})
    else:
        return HttpResponseNotFound()

@login_required
def list_events(request):
    events = User_has_score.objects.all()
    return render(request, 'events.html', {'events': events})