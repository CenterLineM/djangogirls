# -*- coding: utf-8 -*-
# trips/admin.py

from django.contrib import admin
# 註冊Post 這個Model
from .models import Post

# Register your models here.

admin.site.register(Post)
