from django.db import models

# Create your models here.
class Banco(models.Model):
    nome_banco = models.CharField(max_length=250)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome_banco

class Emprestimo(models.Model):
    
    qtd_emprestimo = models.PositiveIntegerField(null=False)
    juros = models.PositiveIntegerField(null=False)
    qtd_parcela = models.PositiveIntegerField(null=False)
    dt_emprestimo = models.DateField(default='1900-01-01')
    banco = models.ForeignKey(Banco,on_delete=models.CASCADE,related_name='emprestimo',
    default='sem banco')

    def __str__(self):
        return self.qtd_emprestimo

class TipoCultura(models.Model):
    nome_cultura = models.CharField(max_length=250)

    def __str__(self):
        return self.nome_cultura

class Agricultor(models.Model):
    nome_agricultor = models.CharField(max_length=250)
    qtd_credito = models.PositiveIntegerField(null=False)
    tipo_cultura = models.ForeignKey(TipoCultura,on_delete=models.CASCADE,related_name='agricultor',
    default='sem plantação')
    emprestimo = models.ManyToManyField(Emprestimo,related_name='agricultor',default='sem emprestimo')

    def __str__(self):
        return self.nome_agricultor
