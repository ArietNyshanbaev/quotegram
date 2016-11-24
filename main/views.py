from django.shortcuts import render
from django.contrib import messages
# from django.core.context_processors import csrf
from .forms import SubscriptionForm
import threading
from django.core.mail import send_mail
from django.conf import settings


def main(request):
	args = {}
	form = SubscriptionForm()
	# Инициализация переменных
	if request.POST:
		form = SubscriptionForm(request.POST)
		if form.is_valid() :
			subscriber = form.save()
			note = u'Новый подписчик :' + subscriber.name + u' Номер телефона : ' + subscriber.telephone_number + u' Эл. почта : ' + subscriber.email
			send_message_thread = threading.Thread(target=send_message, args={note})
			send_message_thread.start()
			messages.info(request, 'Спасибо! Мы добавили Вас в базу данных.')
			form = SubscriptionForm()
	args['form'] = form
	template = 'main/index.html'
	return render(request, template, args)

def send_message(note):
	send_mail('Zoffice Subscription', note,
		settings.EMAIL_HOST_USER, ['zoffice.co@gmail.com'], fail_silently=True)