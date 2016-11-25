# django core packages imports 
from django.shortcuts import redirect, get_object_or_404, render
from django.core.urlresolvers import reverse , reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings
# importing project modules 
from custom_code.decorators import logout_required
from quote.models import Quote

@logout_required
def signin(request, key='main'):
	""" SignIn view in order to auhorize users """
	args={}
	if request.GET.get('next', ''):
		messages.info(request, 'You have to be authorized in order to do this action.')

	if request.POST:
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				# check if we got next value
				next_link = request.POST.get('next', '')
				if next_link != '' :
					return redirect(next_link)
				return redirect(reverse('main:main'))
			else:
				note = ''
				messages.info(request, 'Your account banned.')
		else:
			messages.info(request, 'User name and password missmatch, try again. ')

	template = 'auths/signin.html'
	return render(request, template, {})

@logout_required
def signup(request):
	""" SignUp view in order to auhorize users """
	args={}

	if request.POST:
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		password2 = request.POST.get('password2','')
		# Validation of Username and password
		if User.objects.filter(username=username).exists():
			messages.info(request, 'This username is already used. ')
			return redirect(reverse('auths:signup'))
		if password != password2:
			messages.info(request, 'Passwords are not same.')
			return redirect(reverse('auths:signup'))
		User.objects.create_user(username=username, password=password)
		user_login = authenticate(username=username, password=password)
		login(request, user_login)
		messages.info(request, 'You have successfully Registered. ')
		return redirect(reverse('main:main'))
	template = 'auths/signup.html'
	return render(request, template, {})

@login_required(login_url=reverse_lazy('auths:signin'))
def signout(request):
	""" Signout view """
	logout(request)
	return redirect(reverse("main:main"))

@login_required(login_url=reverse_lazy('auths:signin'))
def profile(request):
	""" Profile view """
	args = {}
	args['quotes'] = Quote.objects.filter(user=request.user).order_by('-id')
	args['profile'] = True
	template = 'auths/profile.html'
	return render(request, template, args)