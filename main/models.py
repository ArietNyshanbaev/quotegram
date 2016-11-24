from __future__ import unicode_literals

from django.db import models

class Subscriber(models.Model):
	""" Table to save subscribed users """
	name = models.CharField(' Имя ', max_length=100)
	telephone_number = models.CharField(' Номер телефона ', max_length=100)
	email = models.CharField(' Email ', max_length=100)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = "Подписчик"
		verbose_name_plural = "Подписчики"