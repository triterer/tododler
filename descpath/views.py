from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Messages

@csrf_exempt
def registration(request):
    recieved = json.loads(request.body)
    Uname = recieved['name']
    Upassword = recieved['password']
    try:
    	User.objects.get(username = Uname)
    	return HttpResponse('already registred')
    except User.DoesNotExist:
	    User.objects.create_user(username = Uname,  password = Upassword)
	    return HttpResponse('succes')

@csrf_exempt
def authentification(request):
	recieved = json.loads(request.body)
	Uname = recieved['name']
	Upassword = recieved['password']
	us = authenticate(username = Uname, password = Upassword)
	if us is not None:
		ret1 = User.objects.get(username = Uname)
		ret = Messages.objects.filter(toUser = ret1.id)
		count = Messages.objects.filter(toUser = ret1.id).count()
		answer = {'count':str(count)}
		asd = 0
		for i in ret:
			answer.update({'text'+str(asd):i.text})
			answer.update({'todate'+str(asd):str(i.toDate)})
			asd+=1
		answer = json.dumps(answer)
		return HttpResponse(answer, content_type='application/json')
	else:
		return HttpResponse('not registred')


@csrf_exempt
def create_mes(request):
	try:
		recieved = json.loads(request.body)
		us = User.objects.get(username = recieved['toUser'])
		Messages.objects.create(toUser=us, text = recieved['text'], toDate = recieved['toDate'])
		return HttpResponse('1')
	except:
		return HttpResponse('no such user')


