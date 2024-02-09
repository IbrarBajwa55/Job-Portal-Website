from django.urls import path
from .views import Job_List

urlpatterns = [
    path('joblist/', Job_List.as_view(), name='joblist'),
    
]