from tkinter import CASCADE
from django.db import models



# Create your models here.
class Job_detail(models.Model):
    job_name = models.CharField(max_length=20)
    matching_grade = models.CharField(max_length=10)
    salary = models.IntegerField(default=0)
    working_pattern = models.CharField(max_length=20)
    requirement = models.CharField(max_length=200)
    twojob_possiblity = models.CharField(max_length = 10)
    mainly_do = models.CharField(max_length=1000)
    welfare = models.CharField(max_length=500)
    working_env = models.CharField(max_length= 500)

    def __str__(self):
        return self.job_name


class dupl(models.Model):
    name = models.CharField(max_length=20)
    grade = models.CharField(max_length=10)
    salaryy = models.IntegerField(default=0)
    pattern = models.CharField(max_length=20)
    requirementt = models.CharField(max_length=200)
    possiblity = models.CharField(max_length = 10)

    detaill = models.ForeignKey(Job_detail, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
