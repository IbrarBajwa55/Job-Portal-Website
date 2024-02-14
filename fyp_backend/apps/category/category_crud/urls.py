from django.urls import path,include
from .views import CategoryViewSet
from rest_framework import routers


router= routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
# categories/{category_id}/total_jobs/  for no of jobs



urlpatterns = [    
    path('',include(router.urls))
      
]
