from django.db import models
from datetime import datetime

class Schedule(models.Model):

    DURATION_CHOICES =(
        ('30:00','30:00'),
        ('01:00:00','1:00:00'),
        ('01:30:00','1:30:00'),
        ('02:00:00','2:00:00'),
        ('02:30:00','2:30:00'),
        ('03:00:00','3:00:00'),
    )    

    schedule_id = models.BigAutoField('Id', primary_key=True)
    schedule_topic = models.CharField('Tópico', max_length=30, blank=False,null=False)
    schedule_date_hour = models.DateTimeField('Data Hora inicial', blank=False, null=False)
    schedule_name_creator = models.CharField('Nome do criador', max_length=100, blank=False, null=False)
    schedule_name_receiver = models.CharField('Nome do recebidor', max_length=100, blank=False, null=False)
    schedule_meet_link = models.URLField('Link de reunião',max_length=150 ,blank=False, null=False)
    schedule_meet_location = models.CharField('Local da Reunião',max_length=50 ,blank=False, null=False)
    schedule_description =  models.CharField('Descrição', max_length=100,blank=True,null=True)
    schedule_duration = models.CharField('Duração', default='30:00',max_length=8, choices=DURATION_CHOICES, blank=False, null=False)

    def __str__(self):
        return f'{self.schedule_topic}'
    
class DelSchedule(models.Model):

    delschedule_id = models.CharField('Id', primary_key=True, max_length=50)
    delschedule_topic = models.CharField('Tópico', max_length=30,blank=False,null=False)
    delschedule_date_hour = models.DateTimeField('Data Hora inicial', blank=False, null=False)
    delschedule_name_creator = models.CharField('Nome do criador', max_length=100, blank=False, null=False)
    delschedule_name_receiver = models.CharField('Nome do recebidor', max_length=100, blank=False, null=False)
    delschedule_meet_link = models.URLField('Link de reunião',max_length=150 ,blank=False, null=False)
    delschedule_meet_location = models.CharField('Local da Reunião',max_length=50 ,blank=False, null=False)
    delschedule_description =  models.CharField('Descrição', max_length=100,blank=True,null=True)
    delschedule_duration = models.CharField('Duração', default='30:00',max_length=8, choices=Schedule.DURATION_CHOICES, blank=False, null=False)
    delschedule_dt_now = models.DateTimeField('Data e hora atuais', default=datetime.now())
    delschedule_ip = models.CharField('Ip',max_length=50)
    delschedule_browser = models.CharField('Browser', max_length=100)