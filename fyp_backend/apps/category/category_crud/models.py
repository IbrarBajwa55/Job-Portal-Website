from django.db import models

# Create your models here.

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    # url = models.CharField(max_length=100)
    image=models.ImageField( upload_to='uploaded_logo')

    def __str__(self):
        return self.title

