from django.db import models

# Create your models here.


class busan_employment(models.Model):
    title = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    job_metas = models.CharField(max_length=200)
    apply = models.CharField(max_length=200)
    edu = models.CharField(max_length=200)
    emp_type = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    pay = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title