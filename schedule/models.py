from django.db import models
from home.models import UserManager, UserCollaborator
from datetime import datetime

class Schedule(models.Model):

    schedule_id = models.BigAutoField('Id', primary_key=True)
    schedule_manager_id = models.ForeignKey(UserManager, on_delete=models.CASCADE)
    schedule_collaborator_id = models.ForeignKey(UserCollaborator, on_delete=models.CASCADE)
    schedule_name_manager = models.CharField('Nome do Gerente', max_length=100)
    schedule_name_collaborator = models.CharField('Nome do Colaborador', max_length=100)
    schedule_topic = models.CharField('Título', max_length=50)
    schedule_date = models.CharField('Data')
    schedule_hour = models.CharField('Hora')
    schedule_meet_location = models.CharField('Local da Reunião', max_length=100)
    schedule_description =  models.CharField('Descrição', max_length=350)
    schedule_duration = models.CharField('Duração', max_length=2)
    schedule_status = models.BooleanField("STATUS", default=False)

    def __str__(self):
        return str(self.schedule_id)
    
