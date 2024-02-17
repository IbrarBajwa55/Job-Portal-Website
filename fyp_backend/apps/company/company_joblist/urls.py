# myapp/urls.py
from django.urls import path
from .views import JobsInCompanyView

urlpatterns = [
    # ... (other URL patterns)
    path('companies/<int:company_id>/jobs/', JobsInCompanyView.as_view(), name='jobs-in-company'),
]
