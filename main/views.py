from django.shortcuts import render
from django.contrib import messages
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
		messages.info(request, 'You have successfully crated a quote.')
	template = 'main/create_quote.html'
	return render(request, template, {})
