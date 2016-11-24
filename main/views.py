from django.shortcuts import render,get_object_or_404 ,redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from quote.models import Quote

def main(request):
	""" Main page view """
	template = 'main/index.html'
	return render(request, template, {})

def top_ten(request):
	""" Top ten votes view """
	args = {}
	args['quote'] = Quote.objects.all().order_by('count_vote')[:10]
	template = 'main/top_ten.html'
	return render(request, template, args)

def flop_ten(request):
	""" Flop ten votes view """
	args = {}
	args['quote'] = Quote.objects.all().order_by('-count_vote')[:10]
	template = 'main/flop_ten.html'
	return render(request, template, args)

def last_quotes(request):
	""" Flop ten votes view """
	args = {}
	args['quote'] = Quote.objects.all().order_by('-id')[:10]
	template = 'main/last_quotes.html'
	return render(request, template, args)