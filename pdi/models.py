from django.db import models
from home.models import UserManager, UserCollaborator
from datetime import datetime

class Planning(models.Model):
    def data():
        data = datetime.now()
        dia = data.day
        mes = data.month
        ano = data.year
        return f'{dia}/{mes}/{ano}'

    def time():
        time = datetime.now()
        hora = time.hour
        minutos = time.minute
        return f'{hora}:{minutos}'

    planning_id =  models.BigAutoField('ID', primary_key=True)
    planning_manager_id = models.ForeignKey(UserManager, on_delete=models.CASCADE)
    planning_collaborator_id = models.ForeignKey(UserCollaborator, on_delete=models.CASCADE)
    planning_name_manager = models.CharField('Nome do Gerente', max_length=50)
    planning_name_collaborator =  models.CharField('Nome do Colaborador', max_length=50)
    planning_title = models.CharField('Título', max_length=100)
    planning_goals = models.CharField('Meta', max_length=200)
    planning_status = models.CharField('Status', default='EM ANDAMENTO', max_length=100)
    planning_progess = models.IntegerField('Progresso')
    planning_description = models.CharField('Descrição', max_length=300)
    planning_resource = models.CharField('Recursos', max_length=100)    
    planning_date = models.CharField('Data', default=data)
    planning_hour = models.CharField('Hora', default=time)
    planning_final_date = models.CharField('Data final')
    planning_final_hour = models.CharField('Hora final')

    def __str__(self):
        return f'{self.planning_title}'
