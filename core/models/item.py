from django.db import models


class Tipo(models.Model):
    nome = models.CharField(max_length=100, verbose_name="NOME")

    def __str__(self):
        return self.nome


class Item(models.Model):
    nome = models.CharField(max_length=100, verbose_name="NOME")
    tipo = models.ForeignKey(Tipo, models.DO_NOTHING, related_name='item_tipo')
    peso = models.PositiveIntegerField()

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return '%s (%s)' % (self.nome, self.tipo.nome)
