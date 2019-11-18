from django.shortcuts import render
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
			return render(request, 'allpage.html/', { 'messages':Messages.objects.filter(toUser = user.id) })
	else:
		return render(request, 'regpage.html')





@login_required(login_url='logpage.html')
def show_all(request, usname):
	us = User.objects.get(username = usname)
	posts = Messages.objects.get(toUser = us)
	return render(request, 'allpage.html', {'posts':posts})




def loguser(request):
	if request.method == 'POST':
		form = {'username':request.POST['username'], 'password':request.POST['password']}
		user = authenticate(username = form['username'], password = form['password'])
		if user is not None:
			login(request, user)
			return render(request, 'allpage.html', {'messages':Messages.objects.filter(toUser = user.id)})
		else:
			form['errors'] = "Wrong password or username"
			return render(request, 'logpage.html', {'form':form})
	else:
		return render(request, 'logpage.html')