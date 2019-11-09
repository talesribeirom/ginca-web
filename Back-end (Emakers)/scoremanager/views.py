from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from operator import itemgetter
import json
from django.shortcuts import (
	render,
	redirect
)
from .forms import (
	Score_Form,
	Apply_Score_Form
)
from .models import (
	Score,
	User,
	User_has_score
)
from threading import Thread
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# Função que envia email ao usuário penalizado
def email_sender(input_message, email_to):

    to = email_to
    gmail_user = 'gincaweb@gmail.com'
    gmail_pwd = 'gincaweb123'
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_pwd)
    header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:Penalidade recebida! \n'
    input_message = input_message
    msg = header + input_message 
    smtpserver.sendmail(gmail_user, to, msg)
    smtpserver.close()

# Função que retorna o ranking de todos os usuários
def get_ranking():
	users = User.objects.all()
	total_score_users = {}
	for user in users:
		sum_score_user = 0
		for user_has_score in user.user_has_scores.all():
			sum_score_user += user_has_score.score.equivalent_score
		total_score_users[user.username] = sum_score_user

	ranking = sorted(total_score_users.items(), key=itemgetter(1), reverse=True)

	return ranking

@login_required
def list_ranking(request):
	ranking = get_ranking()
	return render(request, 'ranking.html', {'ranking': ranking})

# Função para aplicar bonificação a um usuário, só pode ser chamada por um administrador
@login_required
def apply_bonus(request, id_user):
	if request.user.is_superuser:
		userAux = User.objects.get(pk=id_user)
		form = Apply_Score_Form(request.POST)
		scores = Score.objects.filter(score_specification='B')

		if request.POST:
			mutable = request.POST._mutable
			request.POST._mutable = True
			score_data = json.loads(form.data['score'])
			form.data['score'] = score_data['score_id']
			request.POST._mutable = mutable

		if form.is_valid():
			form.save()
			return redirect('url_participants')

		return render(request, 'apply-bonus.html', {'form': form, 'userAux': userAux, 'scores': scores})
	else:
		return HttpResponseNotFound()

# Função que aplica penalidade a um usuário, só pode ser chamada por um administrador
@login_required
def apply_penalty(request, id_user):
    if request.user.is_superuser:
        userAux = User.objects.get(pk=id_user)
        form = Apply_Score_Form(request.POST)
        scores = Score.objects.filter(score_specification='P')

        if request.POST:
            mutable = request.POST._mutable
            request.POST._mutable = True
            score_data = json.loads(form.data['score'])
            form.data['score'] = score_data['score_id']
            request.POST._mutable = mutable

        if form.is_valid():
            form.save()
            email_sender(form.data['score_comment'], userAux.email)
            return redirect('url_participants')

        return render(request, 'apply-penalty.html', {'form': form, 'userAux': userAux, 'scores': scores})
    else:
        return HttpResponseNotFound()

# Função que lista os eventos
@login_required
def list_events(request):
    # Se o usuário for administrador: lista todos eventos
    # Senão: lista somente os eventos relacionados a ele
    if request.user.is_superuser:
      events_list = User_has_score.objects.all()
    else:  
      events_list = User_has_score.objects.filter(user=request.user)
     
    paginator = Paginator(events_list, 9)

    page = request.GET.get('page')
    events = paginator.get_page(page)

    return render(request, 'events.html', {'events': events})