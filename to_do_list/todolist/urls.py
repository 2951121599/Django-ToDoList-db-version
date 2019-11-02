# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  urls.py
# 当前系统日期时间：2019/11/2，11:57 
from django.urls import path, include
from . import views

app_name = 'todolist'
urlpatterns = [
    path('home/', views.home, name='主页'),  # http://127.0.0.1:8000/todo/home/
    path('about/', views.about, name='关于'),  # http://127.0.0.1:8000/todo/about/
    path('edit/<每一件事_id>', views.edit, name='编辑'),  # http://127.0.0.1:8000/todo/edit/1
    path('del/<每一件事_id>', views.delete, name='删除'),  # 删除操作
    path('cross/<每一件事_id>', views.cross, name='划掉'),  # 划掉界面
]
