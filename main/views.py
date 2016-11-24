from django.shortcuts import render,get_object_or_404 ,redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from quote.models import Quote

def main(request):
	""" Main page view """
	args = {}
	quotes = Quote.objects.all()
	args['quotes'] = quotes.order_by('?')[:10]
	template = 'main/index.html'
	return render(request, template, args)

def detailed_quote(request, quote_id):
	""" Main page view """
	args = {}
	args['quote'] = get_object_or_404(Quote, pk=quote_id)
	template = 'main/detailed_quote.html'
	return render(request, template, args)

def top_ten(request):
	""" Top ten votes view """
	args = {}
	quotes = Quote.objects.all()
	args['random_quote'] = quotes.order_by('?')[0]
	args['quotes'] = quotes.order_by('-count_vote')[:10]
	template = 'main/top_ten.html'
	return render(request, template, args)

def flop_ten(request):
	""" Flop ten votes view """
	args = {}
	quotes = Quote.objects.all()
	args['random_quote'] = quotes.order_by('?')[0]
	args['quotes'] = quotes.order_by('count_vote')[:10]
	template = 'main/flop_ten.html'
	return render(request, template, args)

def last_quotes(request):
	""" Flop ten votes view """
	args = {}
	quotes = Quote.objects.all()
	args['random_quote'] = quotes.order_by('?')[0]
	args['quotes'] = quotes.order_by('-count_vote')
	template = 'main/last_quotes.html'
	return render(request, template, args)