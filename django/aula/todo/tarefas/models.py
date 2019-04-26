from django.db import models

# Creat e your models here.
class Categoria(models.Model):
	#verbose_name serve para exibição correta da palavra para o usuário
	nome = models.CharField(max_length=150, verbose_name='Nome') 
	descri = models.TextField(verbose_name='Descrição')
