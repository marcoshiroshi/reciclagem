# Generated by Django 4.2.2 on 2023-09-16 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('morador', '0003_alter_morador_latitude_alter_morador_longitude'),
        ('empresa', '0001_initial'),
        ('catador', '0001_initial'),
        ('core', '0003_tipo_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OrdemServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criada', models.DateTimeField(auto_now_add=True)),
                ('data_solicitada', models.DateTimeField(blank=True, null=True)),
                ('data_buscada', models.DateTimeField(blank=True, null=True)),
                ('data_entregue', models.DateTimeField(blank=True, null=True)),
                ('catador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ordem_servico_catador', to='catador.catador')),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ordem_servico_empresa', to='empresa.empresa')),
                ('morador', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ordem_servico_morador', to='morador.morador')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ordem_servico_status', to='core.statusservico')),
            ],
        ),
        migrations.CreateModel(
            name='ItemServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtd', models.PositiveIntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ordem_servico_item', to='core.item')),
                ('ordem', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='itens_ordem_servico', to='core.ordemservico')),
            ],
        ),
    ]