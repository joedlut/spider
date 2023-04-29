from django.urls.conf import re_path
from jobs import views
from django.urls import path,include

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    #职位列表
    re_path(r'^joblist/',views.job_list,name='joblist'),
    re_path(r'^job/(?P<job_id>\d+)/$',views.detail,name='detail'),

    # /跳转至首页
    re_path(r'^$',views.job_list,name="shouye"),

    path('resume/add/', views.ResumeCreateView.as_view(), name='resume-add'),
    path('resume/<int:pk>',views.ResumeDetailView.as_view(),name='resume-detail'),

    # 添加多语言配置  set-language
    path('i18n/', include('django.conf.urls.i18n')),
    path('sentry-debug/', trigger_error),
]

