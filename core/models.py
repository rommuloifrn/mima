from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class Amigo(AbstractBaseUser):
    bio = models.TextField()
    data_de_nascimento = models.DateField(auto_now=False, auto_now_add=False)
    foto = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    
    #amizades = models.ManyToManyField("app.Amigo") assim seria melhor?

class Amizade(models.Model):
    remetente = models.ForeignKey("core.Amigo", related_name='de_quem_e_amigo', on_delete=models.CASCADE)
    destinatário = models.ForeignKey("core.Amigo", related_name='amigos', on_delete=models.CASCADE)

class Item(models.Model):
    Amigo = models.ForeignKey("core.Amigo", on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    link = models.CharField(max_length=50)
    descricao = models.TextField()