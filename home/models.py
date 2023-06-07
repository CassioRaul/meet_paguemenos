from django.db import models
import string
import random
class UserManager(models.Model):
    def token():
        strings = string.ascii_letters
        punctuation = string.punctuation
        token = strings + punctuation
        return (''.join(random.SystemRandom().choices(token, k=32)))

    manager_id = models.BigAutoField("ID", primary_key=True)
    manager_name = models.CharField("NOME", max_length=50)
    manager_email = models.EmailField("E-MAIL", max_length=254)
    manager_password = models.CharField("SENHA", max_length=50)
    manager_function = models.CharField("FUNÇÃO", max_length=255)
    manager_token = models.CharField("TOKEN", default=token, max_length=32)
    
    def __str__(self) -> str:
        return f'{self.manager_name}'
    
class UserCollaborator(models.Model):
    def token():
        strings = string.ascii_letters
        punctuation = string.punctuation
        token = strings + punctuation
        return (''.join(random.SystemRandom().choices(token, k=32)))
    
    collaborator_id = models.BigAutoField("ID",primary_key=True)
    collaborator_name = models.CharField("NOME", max_length=50)
    collaborator_email = models.EmailField("E-MAIL", max_length=255)
    collaborator_password = models.CharField("SENHA", max_length=50)
    collaborator_function = models.CharField("FUNÇÃO", max_length=255)
    collaborator_token = models.CharField("TOKEN", default=token, max_length=32)
    
    def __str__(self) -> str:
        return f'{self.collaborator_name}'