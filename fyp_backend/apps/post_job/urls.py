from django.urls import path
from .views import PostJobView

urlpatterns = [
    path('postjob/', PostJobView.as_view(), name='postjob'),
    
]