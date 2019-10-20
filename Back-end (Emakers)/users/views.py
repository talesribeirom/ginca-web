from django.shortcuts import render, redirect
from .forms import User_Creation_Form
from django.contrib.auth.decorators import login_required


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
