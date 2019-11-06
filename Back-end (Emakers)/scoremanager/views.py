from django.shortcuts import render
from django.shortcuts import (
	render,
	redirect,
	get_object_or_404
)
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
# from django.db.models import Sum
from operator import itemgetter
import json


@login_required
def create_score(request):
	if request.user.is_superuser:
		form = Score_Form(request.POST or None)

		if form.is_valid():
			form.save()
			return redirect('index')

		return render(request, 'new-score.html', {'form': form})
	else:
		return redirect('index')

@login_required
def update_score(request, id_score):
	if request.user.is_superuser:
		score = Score.objects.get(pk=id_score)
		form = Score_Form(request.POST or None, instance=score)

		if form.is_valid():
			form.save()
			return redirect('index')

		return render(request, 'change-score.html', {'form': form, 'score': score})
	else:
		return redirect('index')

@login_required
def score_detail(request, id_score):
	score = get_object_or_404(Score, pk=id_score)
	return render(request, 'detail-score.html', {'score': score})

@login_required
def delete_score(request, id_score):
	if request.user.is_superuser:
		score = Score.objects.get(pk=id_score)
		score.delete()
		return redirect('index')
	else:
		return redirect('index')

def get_ranking():
	users = User.objects.all()
	total_score_users = {}
	for user in users:
		# total_score_users[user.id] = user.user_has_scores.all().aggregate(Sum('score'))['score__sum']
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
		user = User.objects.get(pk=id_user)
		form = Apply_Score_Form(request.POST)
		scores = Score.objects.all()

		if request.POST:
			mutable = request.POST._mutable
			request.POST._mutable = True
			score_data = json.loads(form.data['score'])
			form.data['score'] = score_data['score_id']
			request.POST._mutable = mutable

		if form.is_valid():
			form.save()
			return redirect('url_participants')

		return render(request, 'apply-bonus.html', {'form': form, 'user': user, 'scores': scores})
	else:
		return redirect('index')

@login_required
def apply_penalty(request, id_user):
    if request.user.is_superuser:
        user = User.objects.get(pk=id_user)
        form = Apply_Score_Form(request.POST)
        scores = Score.objects.all()

        if form.is_valid():
            form.save()
            return redirect('index')

        return render(request, 'apply-penalty.html', {'form': form, 'user': user, 'scores': scores})
    else:
        return redirect('index')

# @login_required
# def apply_score(request, id_user, slug):
# 	if request.user.is_superuser:
# 		if slug == 'bonus':
# 			user = User.objects.get(pk=id_user)
# 			form = Apply_Score_Form(request.POST)

# 			if form.is_valid():
# 				form.save()
# 				return redirect('index')
			
# 			return render(request, 'apply-score.html', {'form': form, 'user': user})
# 		else:
# 			user = User.objects.get(pk=id_user)
# 			form = Apply_Score_Form(request.POST or None, instance=user)

# 			if form.is_valid():
# 				form.save()
# 				return redirect('index')
			
# 			return render(request, 'apply-score.html', {'form': form, 'user': user})
# 	else:
# 		return redirect('index')