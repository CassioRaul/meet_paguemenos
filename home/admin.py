from django.contrib import admin
from .models import UserManager, UserCollaborator
class listManager(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'function')
admin.site.register(UserManager, listManager)

class listCollaborator(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'function')
admin.site.register(UserCollaborator, listCollaborator)
