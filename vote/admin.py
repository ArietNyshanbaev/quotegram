# importing django modules
from django.contrib import admin
# importing Quotes models
from .models import Vote

admin.site.register(Vote)