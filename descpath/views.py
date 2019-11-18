from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Messages
#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

#def detail(request, question_id):
#    return HttpResponse("You're looking at question %s." % question_id)

#def results(request, question_id):
 #   response = "You're looking at the results of question %s."
##    return HttpResponse(response % question_id)

#def vote(request, question_id):
 #   return HttpResponse("You're voting on question %s." % question_id)
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
		answer = {}
		for i in ret:
			answer.update({'text':i.text,'todatee':str(i.toDate)})
		answer = json.dumps(answer)
		#answer = json.loads(answer)
		print (type(answer))
		return HttpResponse(answer, content_type='application/json')
	else:
		return HttpResponse('not registred')

@csrf_exempt
def create_mes(request):
	recieved = json.loads(request.body)
	us = User.objects.get(username = recieved['toUser'])
	Messages.objects.create(toUser=us, text = recieved['text'], toDate = recieved['toDate'])
	return HttpResponse('1')


