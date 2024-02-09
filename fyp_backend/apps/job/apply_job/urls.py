from django.urls import path
from .views import ApplyJobView

urlpatterns = [
    path('applyjob/', ApplyJobView.as_view(), name='applyjob'),
]