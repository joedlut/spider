from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):
    job_type = models.SmallIntegerField()
    job_name = models.CharField(max_length=250)
    job_city = models.SmallIntegerField()
    job_duty = models.TextField()
    job_requirment = models.TextField()
    create_date = models.DateTimeField()
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    modified_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'jobs_job'


class Resume(models.Model):
    username = models.CharField(max_length=135)
    city = models.CharField(max_length=135)
    phone = models.CharField(max_length=135)
    email = models.CharField(max_length=135)
    apply_position = models.CharField(max_length=135)
    born_address = models.CharField(max_length=135)
    bachelor_school = models.CharField(max_length=135)
    master_school = models.CharField(max_length=135)
    doctor_school = models.CharField(max_length=135)
    major = models.CharField(max_length=135)
    degree = models.CharField(max_length=135)
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()
    candidate_introduction = models.TextField()
    work_experience = models.TextField()
    project_experience = models.TextField()
    applicant = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    gender = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'jobs_resume'