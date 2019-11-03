from django.shortcuts import render
from users.models import User
from django.contrib.auth.decorators import login_required
from scoremanager.views import get_ranking

@login_required(login_url='/login/')
def index(request):
    ranking = get_ranking()
    return render(request, 'core/index.html', {'ranking': ranking})