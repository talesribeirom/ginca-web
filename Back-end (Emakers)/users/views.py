from django.shortcuts import (
	render,
	redirect	
)
from django.http import HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.template.defaulttags import register
from .forms import (
	User_Creation_Form,
	User_Change_Form
)
from scoremanager.forms import (
    Score_Form,
	Apply_Score_Form
)
from .models import User
from scoremanager.models import Score
from scoremanager.views import get_ranking


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@login_required
def list_users(request):
    if request.user.is_superuser:
        users = User.objects.all().order_by('username')
        form = User_Creation_Form(request.POST or None)
        score = Score_Form(request.POST or None)
        ranking = get_ranking()
        ranking = dict(ranking)
        print(ranking)
        print(ranking.get(request.user.username))
        if form.is_valid():
            form.save()
            return redirect('url_participants')

        if score.is_valid():
            score.save()
            return redirect('url_participants')

        return render(request, 'participants.html', {'users': users, 'form': form, 'score': score, 'ranking': ranking})
    else:
        return HttpResponseNotFound()

@login_required
def profile_user(request):
    userAtual = User.objects.get(pk=request.user.id)
    form = User_Change_Form(request.POST or None, instance=userAtual)

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'profile.html', {'userAtual': userAtual, 'form': form})