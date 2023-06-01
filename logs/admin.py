from django.contrib import admin
from .models import Logs
class ListLogs(admin.ModelAdmin):
    list_display = ('logs_id', 'logs_date_time', 'logs_desc', 'logs_host',)

admin.site.register(Logs, ListLogs)
