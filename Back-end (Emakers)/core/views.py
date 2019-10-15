from django.shortcuts import render

def indexUser(request):
    return render(request, 'core/index.html')