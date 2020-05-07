# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from embed_video.fields import EmbedVideoField
from django.db import models

# Create your models here.



class Rooms(models.Model):
	GENRE_CHOICES = (('A', 'Availabile'),('NA', 'Not Availabile'),)
	Room_name = models.CharField(max_length=100, blank=True)
	beds = models.CharField(max_length=100, blank=True)
	Price = models.IntegerField(max_length=50,blank=True)
	Availability = models.CharField(max_length=1, choices=GENRE_CHOICES, null=True)
	day = models.CharField(max_length=10,blank=True)

class Event(models.Model):
	Event_Name =models.CharField(max_length=100, blank=True)
	Video_Url = models.CharField(max_length=100, blank=True)
	Descripton = models.CharField(max_length=100, blank=True)
	Package_costs = models.CharField(max_length=100, blank=True)
	Offer_Price = models.CharField(max_length=100, blank=True)

class Visit(models.Model):
	Place_Name = models.CharField(max_length=100, blank=True)
	Images = models.ImageField(upload_to='visit/', null=True,blank=True)
	video = EmbedVideoField(verbose_name="My video", help_text="This is a help text",blank=True)
	Description = models.CharField(max_length=100, blank=True)

class UserPayments(models.Model):
	payment_id = models.IntegerField(max_length=50,blank=True)
	order_id = models.IntegerField(max_length=50,blank=True)
	order_amount = models.IntegerField(max_length=50,blank=True)
	product_info = models.CharField(max_length=100, blank=True)
	is_paid = models.BooleanField(default=False)
	name = models.CharField(max_length=100, blank=True)
	email = models.EmailField(blank=True)