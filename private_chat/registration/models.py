from django.db import models

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField('auth.User', blank=True, null=True, default=None)
	username = models.CharField(max_length=32, blank=True, null=True)
	password = models.CharField(max_length=32, blank=True, null=True)
	email = models.EmailField()

	def __unicode__(self):
		return self.username
