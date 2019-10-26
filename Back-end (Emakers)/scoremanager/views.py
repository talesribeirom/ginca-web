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
	User
)


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


# @login_required
# def apply_bonus(request, id_user):
# 	if request.user.is_superuser:
# 		user = User.objects.get(pk=id_user)
# 		form = Apply_Score_Form(request.POST or None, instance=user)

# 		if form.is_valid():
# 			form.save()
# 			return redirect('index')
		
# 		return render(request, 'apply_bonus.html', {'form': form, 'user': user})
# 	else:
# 		return redirect('index')

# @login_required
# def apply_penalty(request, id_user):
# 	if request.user.is_superuser:
# 		user = User.objects.get(pk=id_user)
# 		form = Apply_Score_Form(request.POST or None, instance=user)

# 		if form.is_valid():
# 			form.save()
# 			return redirect('index')
		
# 		return render(request, 'apply_penalty.html', {'form': form, 'user': user})
# 	else:
# 		return redirect('index')

@login_required
def apply_score(request, id_user, slug):
	if request.user.is_superuser:
		if slug == 'bonus':
			user = User.objects.get(pk=id_user)
			form = Apply_Score_Form(request.POST or None, instance=user)

			if form.is_valid():
				form.save()
				return redirect('index')
			
			return render(request, 'apply-score.html', {'form': form, 'user': user})
		else:
			user = User.objects.get(pk=id_user)
			form = Apply_Score_Form(request.POST or None, instance=user)

			if form.is_valid():
				form.save()
				return redirect('index')
			
			return render(request, 'apply-score.html', {'form': form, 'user': user})
	else:
		return redirect('index')