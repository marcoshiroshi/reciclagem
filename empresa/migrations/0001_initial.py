# Generated by Django 4.2.2 on 2023-09-03 19:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_remove_municipio_modulo_fiscal_remove_municipio_prs'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('data_updated', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=256, verbose_name='Nome da Empresa')),
                ('cnpj', models.CharField(max_length=18, verbose_name='CNPJ')),
                ('telefone_1', models.CharField(help_text='(WHATSAPP)', max_length=18, verbose_name='Telefone 1')),
                ('telefone_2', models.CharField(blank=True, max_length=18, null=True, verbose_name='Telefone 2')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('logradouro', models.CharField(max_length=255, verbose_name='Endereço')),
                ('complemento', models.CharField(blank=True, max_length=255, null=True, verbose_name='Complemento')),
                ('longitude', models.DecimalField(decimal_places=18, help_text='Coordenada geográfica do centro de coleta', max_digits=20, max_length=255, verbose_name='longitude')),
                ('latitude', models.DecimalField(decimal_places=18, help_text='Coordenada geográfica do centro de coleta', max_digits=20, max_length=255, verbose_name='latitude')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.municipio', verbose_name='Município')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='empresa_usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
