from django.db import models


# Creat e your models here.
class Categoria(models.Model):
    # verbose_name serve para exibição correta da palavra para o usuário
    nome = models.CharField(max_length=150, verbose_name='Nome')
    descri = models.TextField(verbose_name='Descrição')

    def __str__(self):
        # função para  retornar o nome definido pelo usuário
        return self.nome


class Tarefa(models.Model):
    PRIORIDADE_CHOICES = (('B', 'Baixa'), ('M', 'Média'), ('A', 'Alta'),)
    nome = models.CharField(max_length=100, verbose_name='Nome')
    descricao = models.TextField(blank=True, verbose_name='Descrição')
    data_final = models.DateField(verbose_name='Data Final')
    prioridade = models.CharField(max_length=1, choices=PRIORIDADE_CHOICES,
                                  verbose_name='Prioridade')
    categoria = models.ForeignKey(Categoria, verbose_name='Categoria')

    def __str__(self):
        return self.nome
