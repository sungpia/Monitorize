# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

from django.http import HttpResponse
from .models import Message

from django.template import loader

def index(request):
	return HttpResponse("Hello World")

@csrf_exempt
def message(request):
	msgg = None 
	if request.method == "POST":
		# TODO(sungpia@me.com): Handle data.
		print(request.POST)
		print(request.POST.get('source'))
		try:	
			msg = Message()
			msg.source = request.POST.get('source', '')
			msg.message_type = request.POST.get('message_type', '')
			msg.message = request.POST.get('message', '')
			msg.save()	
		except:
			print('data not saved')
		return HttpResponse(status=200)
	elif request.method == "GET":
		msgg = Message.objects.all()
		context = {
			'msg': msgg,
		}
		template = loader.get_template('app/index.html')
		print(context)
		return HttpResponse(template.render(context, request))
	return HttpResponse(status=501)
