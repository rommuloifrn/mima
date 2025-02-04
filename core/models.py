from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Amigo(AbstractUser):
    bio = models.TextField(null=True)
    data_de_nascimento = models.DateField(null=True, auto_now=False, auto_now_add=False)
    foto = models.ImageField(null=True, upload_to=None, height_field=None, width_field=None, max_length=None)
    
    def __str__(self):
        return self.username
    
    
    #amizades = models.ManyToManyField("app.Amigo") assim seria melhor?

class Amizade(models.Model):
    remetente = models.ForeignKey("core.Amigo", related_name='de_quem_e_amigo', on_delete=models.CASCADE)
    destinatario = models.ForeignKey("core.Amigo", related_name='amigos', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.rementente) + " é amigo de " + str(self.destinatario)
    

class Sugestao(models.Model):
    amigo = models.ForeignKey("core.Amigo", on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    link = models.CharField(max_length=50)
    descricao = models.TextField()