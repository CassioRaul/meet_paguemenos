from django.db import models
from django.utils import timezone

class Planning(models.Model):
    
    STATUS_CHOICES =(
        ('1','Concluido'),
        ('2','Em atraso'),
        ('3','Em andamento'),
    )
    planning_id =  models.BigAutoField('Id',primary_key=True)
    planning_title = models.CharField('Titulo',max_length=50,blank=False,null=False)
    planning_goals_1 = models.CharField('Meta 1',max_length=200,blank=False,null=True)
    planning_status_1 = models.CharField('status',max_length=1,choices=STATUS_CHOICES,null=False,blank=False)
    planning_goals_2 = models.CharField('Meta 2',max_length=200,blank=True,null=True)
    planning_status_2 = models.CharField('status',max_length=1,choices=STATUS_CHOICES,null=False,blank=True)
    planning_goals_3 = models.CharField('Meta 3',max_length=200,blank=True,null=True)
    planning_status_3 = models.CharField('status',max_length=1,choices=STATUS_CHOICES,null=False,blank=True)
    planning_progess = models.IntegerField('Progresso',default=0,blank=True,null=True)
    planning_final_date = models.DateField('Data final', blank=False, null=False)
    planning_description = models.CharField('Descrição',max_length=300,blank=False, null=False)
    planning_resource = models.CharField('Recursos', max_length=100, blank=False, null=False)
    planning_contributor_name =  models.CharField('Nome do colaborador', max_length=45,blank=False,null=False)
    planning_creator = models.CharField("Criador",max_length=50, blank=False, null=False)
    planning_date = models.DateTimeField('Data/Hora', default=timezone.now, blank=True, db_index=True)

    def __str__(self):
        return f'{self.planning_title}'
    

class DelPlanning(models.Model):

   delplanning_id = models.BigAutoField('id',primary_key=True)
   delplanning_id_origin = models.CharField('Id', max_length=10)
   delplanning_title = models.CharField('Titulo',max_length=50,blank=False,null=False)
   delplanning_goals_1 = models.CharField('Meta 1',max_length=200,blank=False,null=True)
   delplanning_status_1 = models.CharField('status',max_length=1,choices=Planning.STATUS_CHOICES,null=False,blank=False)
   delplanning_goals_2 = models.CharField('Meta 2',max_length=200,blank=True,null=True)
   delplanning_status_2 = models.CharField('status',max_length=1,choices=Planning.STATUS_CHOICES,null=False,blank=False)
   delplanning_goals_3 = models.CharField('Meta 3',max_length=200,blank=True,null=True)
   delplanning_status_3 = models.CharField('status',max_length=1,choices=Planning.STATUS_CHOICES,null=False,blank=False)
   delplanning_progess = models.IntegerField('Progresso',default=0,blank=True,null=True)
   delplanning_final_date_origin = models.DateField('Data final', blank=False, null=False)
   delplanning_description =  models.CharField('Descrição',max_length=300,blank=False, null=False)
   delplanning_resource =  models.CharField('Recursos', max_length=100, blank=False, null=False)
   delplanning_contributor_name = models.CharField('Nome do colaborador', max_length=45,blank=False,null=False)
   delplanning_creator = models.CharField("Criador",max_length=50 ,blank=False, null=False)
   delplanning_date = models.DateField('Data de deleçao', blank=False, null=False)
   delplanning_browser = models.CharField('Navegador',max_length=50,blank=False,null=False)
   delplanning_ip = models.CharField('Ip da máquina',max_length=50,blank=False,null=False)
   

   def __str__(self):
       return f'{self.delplanning_title}'
