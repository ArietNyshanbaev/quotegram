from django.shortcuts import render
from django.contrib import messages

def main(request):
	""" Main page view """
	template = 'quotes/index.html'
	return render(request, template, {})

