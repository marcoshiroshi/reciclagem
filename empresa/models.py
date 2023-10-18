from django.db import models
from core.models import Municipio, Tipo
from usuario.models import User


class Empresa(models.Model):
    date_create = models.DateTimeField(auto_now_add=True)
    data_updated = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, models.DO_NOTHING, related_name='empresa_usuario')
    nome = models.CharField(max_length=256, verbose_name='Nome da Empresa')
    cnpj = models.CharField(max_length=18, verbose_name='CNPJ')
    telefone_1 = models.CharField(max_length=18, verbose_name='Telefone 1', help_text='(WHATSAPP)')
    telefone_2 = models.CharField(max_length=18, verbose_name='Telefone 2', null=True, blank=True)
    cep = models.CharField(max_length=9, verbose_name='CEP')
    logradouro = models.CharField(max_length=255, verbose_name='Endereço')
    complemento = models.CharField(max_length=255, verbose_name='Complemento', null=True, blank=True)
    municipio = models.ForeignKey(Municipio, models.DO_NOTHING, verbose_name='Município')
    longitude = models.DecimalField(max_length=255, max_digits=20, decimal_places=18, verbose_name='longitude', help_text='Coordenada geográfica do centro de coleta')
    latitude = models.DecimalField(max_length=255, max_digits=20, decimal_places=18, verbose_name='latitude', help_text='Coordenada geográfica do centro de coleta')

    def __str__(self):
        return self.nome

    def localizacao(self):
        return [str(self.latitude), str(self.longitude)]


class PontoColeta(models.Model):
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING, related_name='ponto_coleta_empresa')
    tipo_aceito = models.ManyToManyField(Tipo, verbose_name="Tipos de Itens Aceitos")
    longitude = models.DecimalField(max_length=255, max_digits=20, decimal_places=18, verbose_name='longitude', help_text='Coordenada geográfica do ponto de coleta')
    latitude = models.DecimalField(max_length=255, max_digits=20, decimal_places=18, verbose_name='latitude', help_text='Coordenada geográfica do ponto de coleta')

    def __str__(self):
        return '%s - %s' % (self.empresa.nome, self.numero())

    def localizacao(self):
        return [str(self.latitude), str(self.longitude)]

    def numero(self):
        return '{:0>5}'.format(self.id)

    def peso_total_recolhido(self):
        return 0
