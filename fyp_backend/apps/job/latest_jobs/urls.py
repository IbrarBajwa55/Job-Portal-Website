from django.urls import path
from .views import Latest_Jobs

urlpatterns = [
    path('latestjobs/', Latest_Jobs.as_view(), name='latestjobs'),
    
]