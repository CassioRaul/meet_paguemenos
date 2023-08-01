from django.contrib import admin
from .models import Feedback

class ListFeedback(admin.ModelAdmin):
    list_display = ('feedback_id', 'feedback_idschedule', 'feedback_manager_id', 'feedback_collaborator_id', 'feedback_title', 'feedback_manage', 'feedback_collaborator', 'feedback_date', 'feedback_hour', 'feedback_note', 'feedback_evaluate')

admin.site.register(Feedback, ListFeedback)
