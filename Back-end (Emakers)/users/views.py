from django.shortcuts import (
	render,
	redirect,
	get_object_or_404
)
from django.contrib.auth.decorators import login_required
from .forms import (
	User_Creation_Form,
	User_Change_Form
)
from .models import User


@login_required
def create_user(request):
	if request.user.is_superuser:
		form = User_Creation_Form(request.POST or None)

		if form.is_valid():
			form.save()
			return redirect('index')

		return render(request, 'new-user.html', {'form': form})
	else:
		return redirect('index')

@login_required
def update_user(request, id_user):
	if request.user.is_superuser or id_user == request.user.id:
		user = User.objects.get(pk=id_user)
		form = User_Change_Form(request.POST or None, instance=user)

		if form.is_valid():
			form.save()
			return redirect('index')

		return render(request, 'change-user.html', {'form': form, 'user': user})
	else:
		return redirect('index')

@login_required
def user_detail(request, id_user):
	user = get_object_or_404(User, pk=id_user)
	return render(request, 'detail-user.html', {'user': user})

@login_required
def delete_user(request, id_user):
	if request.user.is_superuser:
		user = User.objects.get(pk=id_user)
		user.delete()
		return redirect('index')
	else:
		return redirect('index')

@login_required
def list_users(request):
	users = User.objects.all().order_by('username')
	return render(request, 'participants.html', {'users': users})