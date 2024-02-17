from django.contrib import admin
from .models import PostJob

class PostJobAdmin(admin.ModelAdmin):
    list_display=('job_title','job_location','job_type')
    




admin.site.register(PostJob,PostJobAdmin)
