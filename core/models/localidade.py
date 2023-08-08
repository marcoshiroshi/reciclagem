from django.db import models


class Regiao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="NOME")

    def __str__(self):
        return self.nome


class Estado(models.Model):
    nome = models.CharField(max_length=255, verbose_name="NOME")
    uf = models.CharField(max_length=2, verbose_name="UF")
    regiao = models.ForeignKey(Regiao, models.DO_NOTHING, verbose_name="REGIÃO")

    def __str__(self):
        return self.nome


class Municipio(models.Model):
    nome = models.CharField(verbose_name="NOME", max_length=255)
    estado = models.ForeignKey(Estado, models.DO_NOTHING, verbose_name="ESTADO")
    modulo_fiscal = models.IntegerField(default=0, verbose_name="MÓDULO FISCAL")
    prs = models.BooleanField(default=False)

    def __str__(self):
        nome_str = "[%s] %s" % (self.estado.uf, self.nome)
        return nome_str
