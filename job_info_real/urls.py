from job_info_real import views
from django.urls import URLPattern, path


app_name = 'job_info_real'

urlpatterns = [
    path('',views.index, name='index'),
]