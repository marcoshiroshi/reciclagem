from django.db import models
from core.models import Item
from morador.models import Morador
from catador.models import Catador
from empresa.models import Empresa


class StatusServico(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class StatusItem(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class OrdemServico(models.Model):
    status = models.ForeignKey(StatusServico, models.DO_NOTHING, related_name='ordem_servico_status')
    morador = models.ForeignKey(Morador, models.DO_NOTHING, related_name='ordem_servico_morador')
    catador = models.ForeignKey(Catador, models.DO_NOTHING, related_name='ordem_servico_catador', blank=True, null=True)
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING, related_name='ordem_servico_empresa', blank=True, null=True)
    data_criada = models.DateTimeField(auto_now_add=True)
    data_solicitada = models.DateTimeField(blank=True, null=True)
    data_buscada = models.DateTimeField(blank=True, null=True)
    data_entregue = models.DateTimeField(blank=True, null=True)

    def peso_total_servico(self):
        total = 0
        if hasattr(self, 'itens_ordem_servico'):
            for item in self.itens_ordem_servico.all():
                total += item.peso_total()
        return '%.2f' % total

    def peso_real(self):
        total = 0
        if hasattr(self, 'itens_ordem_servico'):
            for item in self.itens_ordem_servico.all():
                total += item.peso_total() if item.status.nome in ['ACEITO', 'ENTREGUE'] else 0
        return '%.2f' % total

    def peso_descartado(self):
        total = 0
        if hasattr(self, 'itens_ordem_servico'):
            for item in self.itens_ordem_servico.all():
                total += item.peso_total() if item.status.nome == 'NÃO ACEITO' else 0
        return '%.2f' % total

    def materiais_servico(self):
        lista = []
        if hasattr(self, 'itens_ordem_servico'):
            for item in self.itens_ordem_servico.all():
                if item.item.tipo.nome not in lista:
                    lista.append(item.item.tipo.nome)
        return lista

    def numero(self):
        return '{:0>5}'.format(self.id)


class ItemServico(models.Model):
    ordem = models.ForeignKey(OrdemServico, models.DO_NOTHING, related_name='itens_ordem_servico')
    status = models.ForeignKey(StatusItem, models.DO_NOTHING, related_name='itens_status', default=1)
    item = models.ForeignKey(Item, models.DO_NOTHING, related_name='ordem_servico_item', verbose_name='Item para ser reciclado')
    qtd = models.PositiveIntegerField(verbose_name='Quantidade do mesmo item')

    class Meta:
        ordering = ['id']

    def peso_total(self):
        return (self.item.peso * self.qtd)/1000
