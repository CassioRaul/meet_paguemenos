from django.contrib import admin
from .models import UserManager, UserCollaborator
class listManager(admin.ModelAdmin):
    list_display = ('manager_id', 'manager_name', 'manager_email', 'manager_function', 'manager_token')
admin.site.register(UserManager, listManager)

class listCollaborator(admin.ModelAdmin):
    list_display = ('collaborator_id', 'collaborator_name', 'collaborator_email', 'collaborator_function', 'collaborator_token')
admin.site.register(UserCollaborator, listCollaborator)
