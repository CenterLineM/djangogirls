# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

#匯入所需 model , import  Post
from .models import Post

# 匯入頁面
from .models import PostPag


# trips/views.py
# Create your views here.

def hello_world(request):
	return render(request, 'hello_world.html', {
		'current_time': str(datetime.now()),
		})

# 取得所有 posts -- 
#透過 Post.objects.all() 
#從資料庫取得全部的 posts，
#並傳入 home.html 這個 template。

def home(request):
	post_list = Post.objects.all()
	return render(request, 'home.html',{
		'post_list':post_list
		})


# 建立單篇文章的view
def post_detail(request, pk):
	post = Post.objects.get(pk=pk)
	return render(request, 'post.html', {'post': post})



# 初始頁面
# 共用模板
def PageHome(request):
	template = get_template('pagehome.html')
	posts = PostPag.objects.all()
	now = datetime.now()
	html = template.render(local())
	return HttpResponse(html)

