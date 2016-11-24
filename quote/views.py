from django.shortcuts import render,get_object_or_404 ,redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Quote

@login_required(login_url=reverse_lazy('auths:signin'))
def create_quote(request):
	""" Create quote view """
	if request.POST:
		quote_body = request.POST.get('quote_body', '')
		quote = Quote.objects.create(body=quote_body, user=request.user)
		messages.info(request, 'You have successfully crated this quote.')
		return redirect(reverse('main:detailed_quote', kwargs={'quote_id':quote.id}))
	template = 'quote/create_quote.html'
	return render(request, template, {})

@login_required(login_url=reverse_lazy('auths:signin'))
def edit_quote(request, quote_id):
	""" Edit quote view """
	args = {}
	quote = get_object_or_404(Quote, pk=quote_id, user=request.user)

	if request.POST:
		quote_body = request.POST.get('quote_body', '')
		quote.body = quote_body
		quote.save()
		messages.info(request, 'You have successfully edited this quote.')
		return redirect(reverse('main:detailed_quote', kwargs={'quote_id':quote.id}))
	template = 'quote/edit_quote.html'
	args['quote'] = quote
	return render(request, template, args)

@login_required(login_url=reverse_lazy('auths:signin'))
def delete_quote(request, quote_id):
	""" Delete quote view """
	args = {}
	quote = get_object_or_404(Quote, pk=quote_id, user=request.user)
	quote.delete()
	messages.info(request, 'You have successfully deleted your quote.')
	return redirect(reverse('main:main'))


