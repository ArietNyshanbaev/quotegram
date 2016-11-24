# importing django modules
from django.contrib import admin
# importing Quotes models
from .models import Quote

admin.site.register(Quote)