from django.contrib import admin
from .models import Task
# Register your models here.

@admin.register(Task)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'time_sensitive',
                    'time_to_complete','created_at','updated_at']
    list_editable = ['time_sensitive','time_to_complete']
    list_per_page = 10
    search_fields = ['description__icontains']
    list_filter = ['time_sensitive','time_to_complete']

