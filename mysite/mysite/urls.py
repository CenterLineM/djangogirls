# -*- coding: utf-8 -*-

"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf.urls import include, url
from django.contrib import admin
# -*- coding: utf-8 -*-
# 呼叫寫好的App 程式
# 先 import 剛剛寫的 view function：
# 增加動態網址傳送 post_detail
from trips.views import hello_world, home, post_detail

#載入 自創頁面
from trips.views import PageHome


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #測試導向 Hello World
    url(r'^hello/$', hello_world),
    #導向後台管理
    url(r'^admin/', include(admin.site.urls)),

    # 將首頁（正規表達式 ^$）指向 home() 這個 view function
    url(r'^$', home),

    #單頁頁面
    url(r'^post/(?P<pk>\d+)/$', post_detail, name='post_detail'),

    #初始頁面
    url(r'^pagehom/$', PageHome),





]
