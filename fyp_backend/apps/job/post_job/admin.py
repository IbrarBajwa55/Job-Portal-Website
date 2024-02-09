from django.contrib import admin
from .models import PostJob

class PostJobAdmin(admin.ModelAdmin):
    list_display=('job_title','job_location','job_type','upload_logo')
    




admin.site.register(PostJob,PostJobAdmin)

