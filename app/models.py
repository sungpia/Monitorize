# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Message(models.Model):
	MESSAGE_TYPES = (
		('D', 'Debug'),
		('I', 'INFO'),
	)
	source = models.TextField()
	message_type = models.CharField(
		max_length=1,
		choices=MESSAGE_TYPES,
		blank=True,
		default='D',
	)
	time_stamp = models.DateField(auto_now=True)
	message = models.TextField()
