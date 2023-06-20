from django.db import models
from django.utils import timezone
class Feedback(models.Model):
    feedback_iduser= models.BigAutoField(primary_key=True)
    feedback_title = models.CharField('TITULO', max_length=50)
    feedback_manage=models.CharField('GERENTE', max_length=50)
    feedback_collaborator=models.CharField('COLABORADOR', max_length=50)
    feedback_date = models.CharField('DATA/HORA') #, default=timezone.now, blank=True, db_index=True
    # feedback_quest1= models.CharField('Quais são as habilidades de seu liderado?', max_length=100)
    # feedback_quest2 = models.CharField('Qual seu diferencial?', max_length=100)
    # feedback_quest3= models.CharField('O que impede seu desenvolvimento?', max_length= 100)
    # feedback_quest4 = models.CharField('O que pode melhorar?', max_length=100)
    # feedback_quest5 = models.CharField('Quais mudanças pode melhorar seu desempenho?', max_length=100)
    # feedback_quest6 = models.CharField('O que pode atrapalhar seu desempenho?', max_length=100)
    feedback_desc = models.CharField('DESCRIÇÃO', max_length=350)
    feedback_evaluate = models.CharField('AVALIAÇÃO', default=0, blank= False)
        
    def __str__(self):
        return f'{self.feedback_title}'
    
class DeleteFeedback(models.Model):
    delete_feedback_id= models.BigAutoField('ID DE EXCLUSAO',primary_key=True)
    delete_feedback_date_time_end = models.DateTimeField('DATA DA EXCLUSÃO', default=timezone.now, blank=True, db_index=True)
    delete_feedback_ipadress=models.CharField('IP',max_length=20)
    delete_feedback_browser=models.CharField('NAVEGADOR',max_length=20)
    delete_feedback_iduser= models.CharField('ID DO FEEBACK', max_length=50)
    delete_feedback_manage=models.CharField('GERENTE', max_length=50)
    delete_feedback_collaborator=models.CharField('COLABORADOR', max_length=50)
    delete_feedback_title = models.CharField('TITULO', max_length=50)
    # delete_feedback_quest1= models.CharField('Quais são as habilidades de seu liderado?', max_length=100)
    # delete_feedback_quest2 = models.CharField('Qual seu diferencial?', max_length=100)
    # delete_feedback_quest3= models.CharField('O que impede seu desenvolvimento?', max_length= 100)
    # delete_feedback_quest4 = models.CharField('O que pode melhorar?', max_length=100)
    # delete_feedback_quest5 = models.CharField('Quais mudanças pode melhorar seu desempenho?',max_length=100)
    # delete_feedback_quest6 = models.CharField('O que pode atrapalhar seu desempenho?',max_length=100)
    delete_feedback_desc = models.CharField('DESCRIÇÃO', max_length=350)
    delete_feedback_date_time = models.DateTimeField('DATA/HORA', blank=True, db_index=True)
    delete_feedback_evaluate = models.IntegerField('ESTRELAS', default=0, blank= False)
    
    def __str__(self):
        return f'{self.delete_feedback_title}'
