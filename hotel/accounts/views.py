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



def SignUp(request):
	form = SignUpForm(request.POST)
	if form.is_valid():
		first_name = form.cleaned_data['first_name']
		last_name = form.cleaned_data['last_name']
		email = form.cleaned_data['email']
		phone = form.cleaned_data['phone']
		mobile=form.cleaned_data['mobile']
		sex = form.cleaned_data['sex']
		form.save()
		print(form)
		return redirect('home')
	else:
		form = SignUpForm()
		print(form)
	return render(request, 'registration/signup.html', {'form': form})
