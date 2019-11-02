"""to_do_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
# from django.conf.urls import url, include
import todolist.urls

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),  # http://127.0.0.1:8000/admin/后台管理界面
    path('todo/', include(todolist.urls)),  # http://127.0.0.1:8000/todo/  找不到此页面 交给app下的urls去处理
]
