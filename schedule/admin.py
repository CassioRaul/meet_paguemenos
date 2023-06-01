from django.contrib import admin
from .models import Schedule, DelSchedule

class ListSchedule(admin.ModelAdmin):
    list_display = (
        'schedule_id',
        'schedule_topic', 
        'schedule_date_hour',
        'schedule_name_creator', 
        'schedule_meet_link', 
        'schedule_description', 
        'schedule_duration',
        )

class ListDelSchedule(admin.ModelAdmin):
    list_display = (
        'delschedule_id',
        'delschedule_topic', 
        'delschedule_date_hour', 
        'delschedule_name_creator', 
        'delschedule_name_receiver', 
        'delschedule_meet_link', 
        'delschedule_description', 
        'delschedule_duration', 
        'delschedule_dt_now',
        'delschedule_ip',
        'delschedule_browser',
        )
    
admin.site.register(Schedule,ListSchedule)
admin.site.register(DelSchedule, ListDelSchedule)