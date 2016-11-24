# importing django modules
from django.contrib.auth.models import User
from django.db import models

class Quote(models.Model):
	""" Table to save quotes of users """
	body = models.CharField(' Body of quote ', max_length=1000)
	user =  models.ForeignKey(User,  verbose_name=' User of quote ')
	count_vote = models.IntegerField('State of votes', default=0)

	def __unicode__(self):
		return self.user.username + " : " +self.body[:50]

	class Meta:
		verbose_name = "Quote"
		verbose_name_plural = "Quotes"