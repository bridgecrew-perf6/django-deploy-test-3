
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from job_info_detail.models import Job_detail, dupl
# Create your views here.


def index(request):
    job_list = Job_detail.objects.all()
    context = {'job_list': job_list}
    return render(request, 'job_info_detail/index.html', context)

def pages(request,id):
    texts = get_object_or_404(Job_detail, pk=id)
    context = {'texts': texts}
    return render(request, 'job_info_detail/pages.html', context)

def detail(request): #여기서 form의 전달된 값을 받아 job_info_detail/<번호>로 간다
    
    try:
        numb = request.POST['searchEmpCode']
        address = '../../job_info_detail/'+numb
        return redirect(address)
    except:
        job_list = Job_detail.objects.all()
        context = {'job_list': job_list}
        return render(request, 'job_info_detail/index.html',context)
    