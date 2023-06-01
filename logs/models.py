from django.db import models
from django.utils import timezone

class Logs(models.Model):
    logs_id = models.BigAutoField("ID", primary_key=True)
    logs_date_time = models.DateTimeField('DATA/HORA', default=timezone.now, blank=True, db_index=True)
    logs_desc = models.CharField("DESCRIÇÃO", max_length=255)
    logs_host = models.CharField("HOST", max_length=50)

    def __str__(self) -> str:
        return f'{self.logs_desc}'
