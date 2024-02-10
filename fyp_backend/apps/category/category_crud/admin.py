from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display=('cat_id','title','image')
    




admin.site.register(Category,CategoryAdmin)