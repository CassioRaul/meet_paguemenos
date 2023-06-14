from django.contrib import admin
from .models import Planning, DelPlanning

class ListPlanning(admin.ModelAdmin):
    list_display = (
        'schedule_id',
        'planning_id',
        'planning_title',
        'planning_goals_1',
        'planning_status_1',
        'planning_goals_2',
        'planning_status_2',
        'planning_goals_3',
        'planning_status_3',
        'planning_progess',
        'planning_final_date',
        'planning_description',
        'planning_resource',
        'planning_contributor_name',
        'planning_creator',
        'planning_date',
        )
    
admin.site.register(Planning, ListPlanning)

class ListDelPlanning(admin.ModelAdmin):

    list_display =(
        'delplanning_id',
        'delplanning_id_origin',
        'delplanning_title',
        'delplanning_goals_1',
        'delplanning_status_1',
        'delplanning_goals_2',
        'delplanning_status_2',
        'delplanning_goals_3',
        'delplanning_status_3',
        'delplanning_progess',
        'delplanning_final_date_origin',
        'delplanning_description',
        'delplanning_resource',
        'delplanning_contributor_name',
        'delplanning_creator',
        'delplanning_date',
        'delplanning_browser',
        'delplanning_ip',
        )   

admin.site.register(DelPlanning, ListDelPlanning)