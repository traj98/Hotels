# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Rooms(models.Model):
	GENRE_CHOICES = (('A', 'Availabile'),('NA', 'Not Availabile'),)
	Room_name = models.CharField(max_length=100, blank=True)
	beds = models.CharField(max_length=100, blank=True)
	Price = models.IntegerField(max_length=50,blank=True)
	Availability = models.CharField(max_length=1, choices=GENRE_CHOICES, null=True)
	day = models.CharField(max_length=10,blank=True)