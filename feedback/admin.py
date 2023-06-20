from django.contrib import admin
from .models import Feedback #, DeleteFeedback
class ListFeedback(admin.ModelAdmin):
    list_display = ('feedback_iduser', 'feedback_title', 'feedback_manage', 'feedback_collaborator', 'feedback_date', 'feedback_desc', 'feedback_evaluate')

admin.site.register(Feedback, ListFeedback)

# class ListDeleteFeedback(admin.ModelAdmin):
#     list_display = ('delete_feedback_id', 'delete_feedback_date_time_end','delete_feedback_ipadress', 'delete_feedback_browser', 'delete_feedback_iduser', 'delete_feedback_manage' 'delete_feedback_collaborator', 'delete_feedback_title','delete_feedback_date_time', 'delete_feedback_evaluate')

# admin.site.register(DeleteFeedback, ListDeleteFeedback)

