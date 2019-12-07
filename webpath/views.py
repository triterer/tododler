from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def reguser(request):
	if request.method == 'POST':
		form = {'username': request.POST['username'], 'password':request.POST['password']}
		try:
			User.objects.get(username = form['username'])
			form['errors'] = 'User with this name already exist'
			return render(request, 'regpage.html', {'form':form})
		except User.DoesNotExist:
			User.objects.create_user(username = form['username'], password = form['password'])
			user = authenticate(username=form['username'], password = form['password'])
			login(request, user)
			return redirect('show_all')
	else:
		return render(request, 'regpage.html')





@login_required(login_url='logpage.html')
def showall(request):
	us = request.user
	try:
		posreturnts = Messages.objects.filter(toUser = us.id)
		return render(request, 'allpage.html', {'posts':posreturnts})
	except:
		return render(request, 'allpage.html',{'err':'no messages for U'})




def loguser(request):
	if request.method == 'POST':
		form = {'username':request.POST['username'], 'password':request.POST['password']}
		user = authenticate(username = form['username'], password = form['password'])
		if user is not None:
			login(request, user)
			return redirect('/webpath/allpage/')
		else:
			form['errors'] = "Wrong password or username"
			return render(request, 'logpage.html', {'form':form})
	else:
		return render(request, 'logpage.html')


@login_required(login_url='logpage.html')
def create_new(request):
	if request.method == "POST":
		tu = request.user #do you now what time it is?
		form = { 'text':request.POST['text'], 'toDate':request.POST['toDate']}
		Messages.objects.create(toUser = tu, text = form['text'], toDate = form['toDate'])
		return redirect('/webpath/allpage/')
	return render(request,'createmes.html')


