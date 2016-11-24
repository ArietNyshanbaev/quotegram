from django.shortcuts import render,get_object_or_404 ,redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# from quote.models import Quote

def main(request):
	""" Main page view """
	template = 'main/index.html'
	return render(request, template, {})