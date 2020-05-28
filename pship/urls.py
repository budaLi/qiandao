"""pship URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^student_login/$', views.student_login,name="student_login"),
    url('^teacher_login/$', views.teacher_login,name="teacher_login"),
    url('^teacher_index/$', views.teacher_index,name="teacher_index"),
    url('^student_index/$', views.student_index,name="student_index"),
    url('^qiandao/$', views.qiandao,name="qiandao"),
    url('^qiandao_edit/([a-zA-Z0-9.]+)/$', views.edit_qiandao,name="qiandao_edit"),
    url('^qiandao_del/([a-zA-Z0-9.]+)/$', views.delete_qiandao,name="qiandao_del"),

]
