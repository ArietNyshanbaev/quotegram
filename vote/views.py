from django.shortcuts import render,get_object_or_404 ,redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Vote
from quote.models import Quote

@login_required(login_url=reverse_lazy('auths:signin'))
def vote(request, quote_id, type):
	""" Delete quote view """
	args = {}
	quote = get_object_or_404(Quote, pk=quote_id)
	if Vote.objects.filter(quote=quote, user=request.user).exists():
		messages.info(request, 'You have already voted for this quote.')
		return redirect(request.META.get('HTTP_REFERER'))

	if int(type) == 1:
		Vote.objects.create(user=request.user, quote=quote)
		messages.info(request, 'You have successfully upvoted for this quote.')
		quote.count_vote = quote.count_vote + 1
		quote.save()
	else:
		Vote.objects.create(user=request.user, quote=quote, is_upvote=False)
		messages.info(request, 'You have successfully downvoted for this quote.')
		quote.count_vote = quote.count_vote - 1
		quote.save()
	return redirect(request.META.get('HTTP_REFERER'))