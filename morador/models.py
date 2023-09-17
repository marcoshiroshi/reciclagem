from django.db import models
from core.models import Municipio, Genero
from usuario.models import User


class Morador(models.Model):
    date_create = models.DateTimeField(auto_now_add=True)
    data_updated = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, models.DO_NOTHING, related_name='morador_usuario')
    cpf = models.CharField(max_length=14, verbose_name='CPF')
    data_nascimento = models.DateField(verbose_name='Data de nascimento')
    genero = models.ForeignKey(Genero, models.DO_NOTHING, verbose_name='Gênero')
    telefone_1 = models.CharField(max_length=18, verbose_name='Telefone 1', help_text='(WHATSAPP)')
    telefone_2 = models.CharField(max_length=18, verbose_name='Telefone 2', null=True, blank=True)
    cep = models.CharField(max_length=9, verbose_name='CEP')
    logradouro = models.CharField(max_length=255, verbose_name='Endereço')
    complemento = models.CharField(max_length=255, verbose_name='Complemento', null=True, blank=True)
    municipio = models.ForeignKey(Municipio, models.DO_NOTHING, verbose_name='Município')
    longitude = models.DecimalField(max_length=255, max_digits=20, decimal_places=18, verbose_name='longitude', help_text='Coordenada geográfica da sua residência')
    latitude = models.DecimalField(max_length=255, max_digits=20, decimal_places=18, verbose_name='latitude', help_text='Coordenada geográfica da sua residência')

    def __str__(self):
        return self.user.get_full_name().title()

    def endereco(self):
        endereco = '%s - %s, %s %s' % (
            self.municipio.estado.nome,
            self.municipio.nome,
            self.logradouro,
            self.complemento if self.complemento else ''
        )
        return endereco.title()
