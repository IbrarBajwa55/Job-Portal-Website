from django.contrib import admin
from .models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('com_id', 'title', 'description', 'com_logo', 'contact_info')
    search_fields = ('title', 'description', 'contact_info')

admin.site.register(Company, CompanyAdmin)