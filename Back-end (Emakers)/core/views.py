from django.shortcuts import render
from users.models import User
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def index(request):
    users = User.objects.all().order_by('username')
    return render(request, 'core/index.html', {'users': users})