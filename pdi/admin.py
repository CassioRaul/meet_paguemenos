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
        'planning_goals_4',
        'planning_status_4',
        'planning_goals_5',
        'planning_status_5',
        'planning_goals_6',
        'planning_status_6',
        'planning_goals_7',
        'planning_status_7',
        'planning_goals_8',
        'planning_status_8',
        'planning_goals_9',
        'planning_status_9',
        'planning_goals_10',
        'planning_status_10',
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
        'delplanning_goals_4',
        'delplanning_status_4',
        'delplanning_goals_5',
        'delplanning_status_5',
        'delplanning_goals_6',
        'delplanning_status_6',
        'delplanning_goals_7',
        'delplanning_status_7',
        'delplanning_goals_8',
        'delplanning_status_8',
        'delplanning_goals_9',
        'delplanning_status_9',
        'delplanning_goals_10',
        'delplanning_status_10',
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