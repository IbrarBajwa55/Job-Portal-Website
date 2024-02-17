from django.db import models

class Company(models.Model):
    com_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    com_logo = models.ImageField(upload_to='uploaded_logo', null=True, blank=True)
    contact_info = models.CharField(max_length=255)

    def __str__(self):
        return self.title