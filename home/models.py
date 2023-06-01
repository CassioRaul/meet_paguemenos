from django.db import models

class UserManager(models.Model):
    id = models.BigAutoField("ID", primary_key=True)
    name = models.CharField("NOME", max_length=50)
    email = models.EmailField("E-MAIL", max_length=254)
    password = models.CharField("SENHA", max_length=50)
    function = models.CharField("FUNÇÃO", max_length=50)
    
    def __str__(self) -> str:
        return f'{self.name}'
    
class UserCollaborator(models.Model):
    id = models.BigAutoField("ID",primary_key=True)
    name = models.CharField("NOME", max_length=50)
    email = models.EmailField("E-MAIL", max_length=254)
    password = models.CharField("SENHA", max_length=50)
    function = models.CharField("FUNÇÃO", max_length=50)
    
    def __str__(self) -> str:
        return f'{self.name}'