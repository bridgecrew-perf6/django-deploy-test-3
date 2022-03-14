from django.shortcuts import render

from job_info_real.models import busan_employment

# Create your views here.

def index(request):
    job_list = busan_employment.objects.all()
    context = {'job_list': job_list}
    return render(request, 'job_info_real/index.html', context)