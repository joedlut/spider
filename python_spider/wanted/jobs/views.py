from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from jobs.models import Job,Resume
from jobs.models import JobTypes, Cities
from django.http import Http404
import logging
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect


from django.views.generic.detail import DetailView

logger = logging.getLogger(__name__)

def job_list(request):
    job_list = Job.objects.order_by('job_type')

    context = {'job_list':job_list}
    for job in job_list:
        job.city_name = Cities[job.job_city][1]
        job.job_type = JobTypes[job.job_type][1]
        #print(job.job_id)

    #return HttpResponse(template.render(context))
    # 主要有render上下文才能获取用户信息
    return render(request,"joblist.html",context)

def detail(request,job_id):
    try:
        job = Job.objects.get(pk=job_id)
        job.city_name = Cities[job.job_city][1]

    except Job.DoesNotExist:
        return Http404("job does not exist")

    return render(request,'job.html',{'job':job})

class ResumeDetailView(DetailView):
    # 简历详情页
    model = Resume
    template_name = "resume_detail.html"

class ResumeCreateView(LoginRequiredMixin,CreateView):
    template_name = "resume_form.html"
    success_url = "/joblist"
    model = Resume
    fields = ["username", "city", "phone",
              "email", "apply_position", "gender",
              "bachelor_school", "master_school", "major", "degree",
              "candidate_introduction", "work_experience", "project_experience"]

    #从url中传递参数 填充到表单中
    def get_initial(self):
        initial = {}
        for x in self.request.GET:
            initial[x] = self.request.GET[x]
        return initial


    def form_valid(self, form):
        # ??????
        self.object = form.save(commit=False)
        logging.info("def form_valid")
        self.object.applicant = self.request.user
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())




