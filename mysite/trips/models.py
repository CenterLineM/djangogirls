# -*- coding: utf-8 -*-
# trips/models.py
from django.db import models

# 時區套件
from django.utils import timezone


# Create your models here.


class Post(models.Model):
	title = models.CharField(max_length= 100)
	content = models.TextField(blank=True)
	photo = models.URLField(blank=True)
	location = models.CharField(max_length =100)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title.encode('utf8')
		#return self.title

#部落格資料庫
class PostPag(models.Model):
	title = models.CharField(max_length=200)
	slug = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ('-pub_date',)
			

	"""docstring for PostPag"""
	def __unicode__(self):
		return self.title

