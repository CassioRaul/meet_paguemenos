from django.db import models
from home.models import UserManager, UserCollaborator
from schedule.models import Schedule
from datetime import datetime

class Feedback(models.Model):
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
    
    feedback_id = models.BigAutoField(primary_key=True)
    feedback_idschedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    feedback_manager_id = models.ForeignKey(UserManager, on_delete=models.CASCADE)
    feedback_collaborator_id = models.ForeignKey(UserCollaborator, on_delete=models.CASCADE)
    feedback_manage = models.CharField('GERENTE', max_length=50)
    feedback_collaborator = models.CharField('COLABORADOR', max_length=50)
    feedback_title = models.CharField('TÍTULO', max_length=50)
    feedback_date = models.CharField('DATA')
    feedback_hour = models.CharField('HORA')
    feedback_note = models.CharField('ANOTAÇÃO', max_length=350)
    feedback_evaluate = models.CharField('AVALIAÇÃO', max_length=50) #default=0, blank= False
        
    def __str__(self):
        return f'{self.feedback_title}'
