from django.shortcuts import render
from users.models import User


def index(request):
    users = User.objects.all().order_by('username')
    return render(request, 'core/index.html', {'users': users})