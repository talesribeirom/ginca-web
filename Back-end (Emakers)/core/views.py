from django.shortcuts import render
from users.models import User
from django.contrib.auth.decorators import login_required
from scoremanager.views import get_ranking

# Indica que o usuário têm que estar autenticado no sistema
@login_required(login_url='/login/')
def index(request):
    # Retorna o ranking dos usuários para serem apresentados na tela principal
    ranking = get_ranking()
    return render(request, 'core/index.html', {'ranking': ranking})