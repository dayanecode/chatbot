from django.db import models

# Create your models here.

class Resposta(models.Model):
    codigo = models.IntegerField()
    # Opção de Resposta
    valor = models.CharField(max_length=1)
    descricao = models.TextField(blank=False, null=False)
    # Para onde esta ação vai levar dentro do fluxo de navegação
    acao = models.TextField(blank=False, null=False)

class Pergunta(models.Model):
    codigo = models.IntegerField()
    titulo = models.TextField(blank=False, null=False)
    respostas = models.ManyToManyField(Resposta)
    