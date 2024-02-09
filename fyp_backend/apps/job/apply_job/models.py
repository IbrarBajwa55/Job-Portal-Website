from django.db import models

# Create your models here.
class ApplyJob(models.Model):
    full_name=models.CharField(max_length=50)
    contact_email=models.CharField(max_length=50)
    contact_phone_number=models.CharField(max_length=15)
    upload_cv=models.FileField(upload_to='document')
    cover_letter=models.TextField()
