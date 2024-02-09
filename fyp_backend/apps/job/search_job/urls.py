from django.urls import path
from .views import SearchJoblist

urlpatterns = [
   
    path('searchjob/', SearchJoblist.as_view(), name='searchjob'),
]