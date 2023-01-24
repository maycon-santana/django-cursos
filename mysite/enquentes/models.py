from django.db import models

class Questao(models.Model):
    questao_text = models.CharField(max_length=200)
    pub_data = models.DateTimeField('data publicação')

class Escolha(models.Model):
        questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
        escolha_text = models.CharField(max_length=200)
        votos = models.IntegerField(default=0)
