import csv
import datetime
from django.contrib import admin
from interview.models import Candidate
from django.http import HttpResponse
from datetime import datetime
import logging
import interview.candidate_field as cf
from django.db.models import Q
from .dingtalk import send

from jobs.models import Resume

from django.utils.safestring import mark_safe

logger = logging.getLogger(__name__)

exportable_fields = (
'username', 'city', 'phone', 'bachelor_school', 'master_school', 'degree', 'first_result', 'first_interviewer_user',
'second_result', 'second_interviewer_user', 'hr_result', 'hr_score', 'hr_remark', 'hr_interviewer_user')


# Register your models here.
def get_readonly_fields(self, request, obj):
    group_names = self.get_group_names(request.user)

    if 'interviewer' in group_names:
        logger.info("user's group is %s" % group_names)
        logger.info("interviewer is in user's group for %s" % request.user.username)
        return ('first_interviewer_user', 'second_interviewer_user',)
    return ()

def notify_interviewer(modeladmin,request,queryset):
    candidates = ""
    interviewers = ""
    for obj in queryset:
        candidates = obj.username + ";" + candidates
        interviewers = obj.first_interviewer_user.username + ";" + interviewers
    logger.info("候选人 %s 进入面试环节，亲爱的面试官，请准备好面试： %s" % (candidates, interviewers))
    send("候选人 %s 进入面试环节，亲爱的面试官，请准备好面试： %s" % (candidates, interviewers))

def export_model_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    field_list = exportable_fields
    response['Content-Disposition'] = 'attachment; filename=%s-list-%s.csv' % (
        'recruitment-candidates',
        datetime.now().strftime('%Y-%m-%d-%H-%M-%S'),
    )

    # 写入表头
    writer = csv.writer(response)
    writer.writerow(
        [queryset.model._meta.get_field(f).verbose_name.title() for f in field_list],
    )

    for obj in queryset:
        ## 单行 的记录（各个字段的值）， 根据字段对象，从当前实例 (obj) 中获取字段值
        csv_line_values = []
        for field in field_list:
            # 获取对应字段 表示的对象
            field_object = queryset.model._meta.get_field(field)
            # 获取对象的值
            field_value = field_object.value_from_object(obj)
            csv_line_values.append(field_value)
        writer.writerow(csv_line_values)
        logger.error("%s has exported %s candidates" % (request.user.username, len(queryset)))
        logger.error("queryset: %s", queryset)
    return response


export_model_as_csv.short_description = u'导出候选人信息为CSV文件'
notify_interviewer.short_description = u'在钉钉群通知面试官'
export_model_as_csv.allowed_permissions = ('export',)

class CandidateAdmin(admin.ModelAdmin):
    exclude = ('creator', 'created_date', 'modified_date')
    # 注册action
    actions = [export_model_as_csv,notify_interviewer]
    list_display = (
        'username', 'city', 'get_resume', 'bachelor_school', 'first_score', 'first_result', 'first_interviewer_user',
        'second_score',
        'second_result', 'second_interviewer_user', 'hr_score', 'hr_result', 'hr_interviewer_user')
    fieldsets = (
        ('应聘人信息', {'fields': (
            "userid", ("username", "city", "phone"), ("email", "apply_position", "born_address"), ("gender",
                                                                                                   "candidate_remark"),
            ("bachelor_school", "master_school", "doctor_school", "major"), ("degree",
                                                                             "test_score_of_general_ability"),
            "paper_score")}),
        ('第一轮面试信息', {'fields': (
            "first_score", "first_learning_ability", "first_professional_competency", "first_advantage",
            "first_disadvantage", "first_result", "first_recommend_position", "first_interviewer_user",
            "first_remark")}),
        ('第二轮面试信息', {'fields': (
            "second_score", "second_learning_ability", "second_professional_competency",
            "second_pursue_of_excellence", "second_communication_ability",
            "second_pressure_score", "second_advantage", "second_disadvantage", "second_result",
            "second_recommend_position", "second_interviewer_user", "second_remark")}),
        ('HR面试信息', {'fields': (
            "hr_score", ("hr_responsibility", "hr_communication_ability"), ("hr_logic_ability", "hr_potential",
                                                                            "hr_stability"), "hr_advantage",
            "hr_disadvantage", "hr_result", "hr_interviewer_user", "hr_remark")}),
    )
    # 右侧过滤器
    list_filter = (
    'city', 'first_result', 'second_result', 'hr_result', 'first_interviewer_user', 'second_interviewer_user',
    'hr_interviewer_user')
    # 搜索栏
    search_fields = ('city', 'username', 'email', 'bachelor_school', 'phone')
    # 排序
    ordering = ('hr_result', 'second_result', 'first_result',)
    # 要放在最后面，放在前面不会生效，不推荐用readonly_fields
    # readonly_fields = ('first_interviewer_user', 'second_interviewer_user')

    def get_resume(self,obj):
        if not obj.phone:
            return ''
        resumes = Resume.objects.filter(phone = obj.phone)
        if resumes and len(resumes) >0 :
            return mark_safe(u'<a href="/resume/%s" target="_blank">%s</a>' % (resumes[0].id, "查看简历"))

    get_resume.short_description = "查看简历"
    #允许使用超链接标签
    get_resume.allow_tags = True

    #重写的是 candidateadmin的方法
    #list_editable = ('first_interviewer_user','second_interviewer_user',)

    #一面面试官只能编辑一面的信息，二面面试官只能编辑二面的信息
    def get_field_sets(self, request, obj=None):
        #先获取组名
        group_names = self.get_group_names(request.user)
        if request.user == obj.first_interviewer_user and 'interviewer' in group_names:
            return cf.default_fieldsets_first

        if request.user == obj.second_interviewer_user and 'interviewer' in group_names:
            return cf.default_fieldsets_second
        return cf.default_fieldsets

    # 判断用户是否有权限，export 跟 export_model_as_csv.allowed_permissions = ('export',) 一一对应
    #  python .\manage.py makemigrations --settings=settings.local
    #  python .\manage.py migrate --settings=settings.local
    def has_export_permission(self,request):
        opts = self.opts
        # 注意没有引号
        return request.user.has_perm("%s.%s" %(opts.app_label, 'export'))

    # 一面面试官仅填写一面反馈， 二面面试官可以填写二面反馈
    def get_queryset(self, request):
        qs = super(CandidateAdmin,self).get_queryset(request)
        group_names = self.get_group_names(request.user)
        logger.info("def get_query_set %s" %group_names)
        if request.user.is_superuser or 'hr' in group_names:
            return qs
        # first_interviewer_user=request.user 变量顺序不能搞反
        return Candidate.objects.filter(Q(first_interviewer_user=request.user)|Q(second_interviewer_user=request.user))

    def get_list_editable(self,request):
        group_names = self.get_group_names(request.user)
        if request.user.is_superuser or 'hr' in group_names:
            return ('first_interviewer_user','second_interviewer_user')
        return ()
    # admin中没有 get_list_editable方法，重写get_changelist_instance，覆盖list_editable属性
    def get_changelist_instance(self, request):
        self.list_editable = self.get_list_editable(request)
        return super(CandidateAdmin,self).get_changelist_instance(request)

    def get_group_names(self, user):
        group_names = []
        for g in user.groups.all():
            group_names.append(g.name)
        return group_names

    def get_readonly_fields(self, request, obj):
        group_names = self.get_group_names(request.user)

        if 'interviewer' in group_names:
            logger.info("interviewer is in user's group for %s" % request.user.username)
            return ('first_interviewer_user', 'second_interviewer_user',)
        return ()



# 不要忘了注册model
admin.site.register(Candidate, CandidateAdmin)
