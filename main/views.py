from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import get_object_or_404

from .models import Quote

def main(request):
	""" Main page view """
	template = 'main/index.html'
	return render(request, template, {})

def create_quote(request):
	""" Create quote view """
	if request.POST:
		quote_body = request.POST.get('quote_body', '')
		Quote.objects.create(body=quote_body, user=request.user)
		messages.info(request, 'You have successfully crated this quote.')
	template = 'main/create_quote.html'
	return render(request, template, {})

def edit_quote(request, quote_id):
	""" Edit quote view """
	args = {}
	quote = get_object_or_404(Quote, pk=quote_id, user=request.user)

	if request.POST:
		quote_body = request.POST.get('quote_body', '')
		quote.body = quote_body
		quote.save()
		messages.info(request, 'You have successfully edited this quote.')
	template = 'main/edit_quote.html'
	args['quote'] = quote
	return render(request, template, args)

