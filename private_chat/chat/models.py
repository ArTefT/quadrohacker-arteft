# -*- coding:utf-8 -*-
from django.db import models

#TODO: (СОВЕТ) Лучше всего писать самодокументирующий код минимум сокращений в именах переменных,
#              а то через пару месяцев забудешь что это за сокращение

class UserMessage(models.Model): 
	autor = models.ForeignKey("registration.UserProfile")
	date_message = models.DateTimeField(auto_now_add=True)
	text_message = models.TextField()
