# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
from .forms import *



def register(request):
	if request.method == 'POST':
		data = {}
		username = request.POST.get('username')
		if(request.POST.get('firstname')):
			data['firstname']=request.POST.get('firstname')
		if (request.POST.get('lastname')):
			data['lastname'] = request.POST.get('lastname')
		if (request.POST.get('phone')):
			data['phone'] = request.POST.get('phone')
		if (request.POST.get('mobile')):
			data['mobile'] = request.POST.get('mobile')
		if (request.POST.get('sex')):
			data['sex'] = request.POST.get('sex')
		user = User.objects.create(email=username,username=username,password='admin')
		userdata = User.objects.filter(username=username)
		##if userdata:
		##	userid = userdata.id
		##userextra_data = UserProfile.objects.create(fieldname=fieldvalue,fieldname1=fieldvalue1,user=userid)
		userdata1 = UserProfile.objects.filter(user=user).update(**data)
		userdata = UserProfile.objects.get(user=user)
		return render(request, 'home.html')
	else:
		return render(request, 'registration/signup.html',{})

def logout_user(request):
	logout(request)
	return redirect('login')



def login_user(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		print(user)
		if user is not None:
			login(request, user)
			return redirect("/")
		else:
			msg = 'incorrect details'
			return render(request, 'login.html', {'msg': msg})
	else:
		msg = ''
		return render(request, 'login.html', {'msg': msg})


def user_edit(request,id):
	user1 = UserProfile.objects.get(pk=id)
	if request.method == 'POST':
		form = Incidentedit(request.POST, instance=user1)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = Incidentedit(instance=user1)
		return render(request, 'incidentedit.html',{'form': form})
