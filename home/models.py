from django.db import models
import string
import random
class UserManager(models.Model):
    def token():
        strings = string.ascii_letters
        number = "0123456789"
        # punctuation = string.punctuation
        token = strings + number
        return (''.join(random.SystemRandom().choices(token, k=12)))
    
    def idGerente():
        number = "0123456789"
        return (''.join(random.SystemRandom().choices(number, k=4)))

    def upload_image(instance, filename):
        return f'{instance.manager_id}-{filename}'

    manager_id = models.BigAutoField("ID", default=idGerente, primary_key=True)
    manager_name = models.CharField("NOME", max_length=50)
    manager_email = models.EmailField("E-MAIL", max_length=254)
    manager_function = models.CharField("FUNÇÃO", max_length=255)
    manager_token = models.CharField("TOKEN", default=token, max_length=12)
    manager_image = models.ImageField("IMAGEM GERENTE", upload_to=upload_image)
    
    def __str__(self) -> str:
        return str(self.manager_id)
    
class UserCollaborator(models.Model):
    def token():
        strings = string.ascii_letters
        number = "0123456789"
        # punctuation = string.punctuation
        token = strings + number
        return (''.join(random.SystemRandom().choices(token, k=12)))
    
    def idColaborador():
        number = "0123456789"
        return (''.join(random.SystemRandom().choices(number, k=4)))
    
    def upload_image(instance, filename):
        return f'{instance.collaborator_id}-{filename}'
    
    collaborator_id = models.BigAutoField("ID", default=idColaborador, primary_key=True)
    collaborator_name = models.CharField("NOME", max_length=50)
    collaborator_email = models.EmailField("E-MAIL", max_length=255)
    collaborator_function = models.CharField("FUNÇÃO", max_length=255)
    collaborator_token = models.CharField("TOKEN", default=token, max_length=12)
    collaborator = models.ImageField("IMAGEM GERENTE", upload_to=upload_image)
    
    def __str__(self) -> str:
        return str(self.collaborator_id)