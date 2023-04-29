"""wanted URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

#多语言翻译
from django.utils.translation import gettext as _
# url 已经被废弃
from django.urls.conf import re_path as url

urlpatterns = [
    url(r'^', include('jobs.urls')),
    path('admin/', admin.site.urls),
    # https://blog.csdn.net/weixin_43883625/article/details/127350853
    path('accounts/', include('registration.backends.simple.urls')),
    #path('grappelli', include('grappelli.urls'))
]

admin.site.site_header = _('果冻科技招聘管理系统')