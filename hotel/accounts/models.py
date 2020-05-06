# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from phone_field import PhoneField
# Create your models here.



class UserProfile(models.Model):
	user = models.ForeignKey(User, unique=True,on_delete=models.CASCADE,default=True)
	GENRE_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'),
    )
	firstname = models.CharField(max_length=100, blank=True)
	lastname = models.CharField(max_length=100, blank=True)
	email =models.EmailField(blank=True)
	phone = PhoneField(blank=True)
	mobile = PhoneField(blank=True)
	sex =  models.CharField(max_length=1, choices=GENRE_CHOICES, null=True)
