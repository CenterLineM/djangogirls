# -*- coding: utf-8 -*-
# trips/admin.py

from django.contrib import admin
# 註冊Post 這個Model
from .models import Post

#部落格
from .models import PostPag

# Register your models here.

admin.site.register(Post)


#v顯示日期和時間
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'pub_date')

# 納入管理
admin.site.register(PostPag, PostAdmin)