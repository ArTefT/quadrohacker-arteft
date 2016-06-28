from django.db import models
from datetime import datetime

class UserMessage(models.Model):
	user_msg = models.ForeignKey("registration.UserProfile")
	date_msg = models.DateTimeField(auto_now_add=True)
	text_msg = models.TextField()
