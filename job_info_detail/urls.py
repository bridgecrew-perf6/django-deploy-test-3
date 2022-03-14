from job_info_detail import views
from django.urls import URLPattern, path


app_name = 'job_info_detail'

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:id>/',views.pages, name='pages'),
    path('detail/', views.detail, name='detail'),
]