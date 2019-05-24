# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Message(models.Model):
	source = models.TextField()
	message_type = models.CharField(max_length=16)
	time_stamp = models.DateField(auto_now=True)
	message = models.TextField()
