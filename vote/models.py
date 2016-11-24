# importing django modules
from django.contrib.auth.models import User
from django.db import models
from quote.models import Quote

class Vote(models.Model):
	""" Table to save quotes of users """
	user = models.ForeignKey(User,  verbose_name=' User who votes ')
	quote = models.ForeignKey(Quote,  verbose_name=' Quote of vote ')
	is_upvote = models.BooleanField('is vote positive?', default=True)

	def __unicode__(self):
		return  self.quote + " : " + self.is_upvote

	class Meta:
		verbose_name = "Vote"
		verbose_name_plural = "Votes"