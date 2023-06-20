from django.contrib import admin
from .models import FeedbackG, DeleteFeedbackG, FeedbackC, DeleteFeedbackC

class ListFeedbackG(admin.ModelAdmin):

    list_display = ('feedback_iduser', 'feedback_title', 'feedback_manage', 'feedback_collaborator', 'feedback_date','feedback_quest1',  'feedback_quest2', 'feedback_quest3','feedback_quest4',  'feedback_quest5', 'feedback_quest6','feedback_note', 'feedback_evaluate')

admin.site.register(FeedbackG, ListFeedbackG)

class ListDeleteFeedbackG(admin.ModelAdmin):
    list_display = ('delete_feedback_id', 'delete_feedback_date_time_end','delete_feedback_ipadress', 'delete_feedback_browser', 'delete_feedback_iduser', 'delete_feedback_manage','delete_feedback_collaborator', 'delete_feedback_title','delete_feedback_quest1', 'delete_feedback_quest2','delete_feedback_quest3', 'delete_feedback_quest4', 'delete_feedback_quest5','delete_feedback_quest6',  'delete_feedback_note', 'delete_feedback_date_time', 'delete_feedback_evaluate')

admin.site.register(DeleteFeedbackG, ListDeleteFeedbackG)

class ListFeedbackC(admin.ModelAdmin):

    list_display=('feedback_iduser', 'feedback_title', 'feedback_manage', 'feedback_collaborator', 'feedback_date', 'feedback_quest1', 'feedback_quest2', 'feedback_quest3', 'feedback_note','feedback_evaluate', )

admin.site.register(FeedbackC, ListFeedbackC)

class ListDeleteFeedbackC(admin.ModelAdmin):
   list_display = ('delete_feedback_id', 'delete_feedback_date_time_end','delete_feedback_ipadress', 'delete_feedback_browser', 'delete_feedback_iduser', 'delete_feedback_manage','delete_feedback_collaborator', 'delete_feedback_title','delete_feedback_quest1', 'delete_feedback_quest2','delete_feedback_quest3', 'delete_feedback_date_time', 'delete_feedback_evaluate','delete_feedback_note',)
admin.site.register(DeleteFeedbackC, ListDeleteFeedbackC)