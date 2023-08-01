from django.contrib import admin
from .models import Schedule
class ListSchedule(admin.ModelAdmin):
    list_display = (
        'schedule_id',
        'schedule_manager_id',
        'schedule_collaborator_id',
        'schedule_name_manager',
        'schedule_name_collaborator',
        'schedule_topic', 
        'schedule_date',
        'schedule_hour',
        'schedule_meet_location',
        'schedule_description', 
        'schedule_duration',
        'schedule_status',
        )
    
admin.site.register(Schedule, ListSchedule)
