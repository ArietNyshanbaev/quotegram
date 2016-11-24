from django.shortcuts import redirect
from django.core.urlresolvers import reverse

def logout_required(f):
	def wrap(request, *args, **kwargs):
		if request.user.is_authenticated() :
			return redirect(reverse('main:main')) 
		return f(request, *args, **kwargs)
	wrap.__doc__=f.__doc__
	wrap.__name__=f.__name__
	return wrap
