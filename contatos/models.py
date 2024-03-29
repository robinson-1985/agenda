from django.db import models
from django.utils import timezone


class Contato(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d', blank=True) # Adiciona o campo foto


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
