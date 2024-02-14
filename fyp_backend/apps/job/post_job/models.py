from django.db import models
from apps.category.category_crud.models import Category

# Create your models here.
class PostJob(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_title=models.CharField(max_length=50)
    job_type=models.CharField(max_length=50 ,choices=(
                                   ('REMOTE','REMOTE'),
                                   ('ON_SITE','ON_SITE')
          ))
    job_location=models.CharField(max_length=150)
    job_category=models.ForeignKey(Category, on_delete=models.CASCADE)
    application_deadline=models.CharField(max_length=150)
    job_description=models.TextField()
    upload_logo=models.ImageField( upload_to='uploaded_logo')
    company_name=models.CharField(max_length=50)
    company_description=models.TextField()
    how_to_apply=models.CharField(max_length=100)
    contact_email=models.CharField(max_length=50)
    contact_phone=models.CharField(max_length=15)
