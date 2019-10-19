from django.shortcuts import render, redirect
from .forms import (
	UserCreationForm,
)

def indexUser(request):
    return render(request, 'core/index.html')

def novo_usuario(request):
	form = UserCreationForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('index')

	return render(request, 'core/cadastro_usuario.html', {'form': form})