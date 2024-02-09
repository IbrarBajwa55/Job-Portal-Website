from django.contrib import admin
from .models import ApplyJob

class ApplyJobAdmin(admin.ModelAdmin):
    list_display=('id', 'full_name', 'contact_email', 'contact_phone_number', 'upload_cv', 'cover_letter')
    




admin.site.register(ApplyJob,ApplyJobAdmin)

