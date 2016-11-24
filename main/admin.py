from django.contrib import admin

from .models import Subscriber

class SubscriberAdmin(admin.ModelAdmin):
	""" Класс Регистрации Админки для Клеинтов """
	list_display = ('name', 'telephone_number', 'email')
admin.site.register(Subscriber, SubscriberAdmin)