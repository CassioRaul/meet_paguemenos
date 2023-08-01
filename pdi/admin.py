from django.contrib import admin
from .models import Planning

class ListPlanning(admin.ModelAdmin):
    list_display = (
        'planning_id',
        'planning_name_manager',
        'planning_name_collaborator',
        'planning_title',
        'planning_goals',
        'planning_status',
        'planning_progess',
        'planning_description',
        'planning_resource',
        'planning_date',
        'planning_hour',
        'planning_final_date',
        'planning_final_hour',
        )
    
admin.site.register(Planning, ListPlanning)
