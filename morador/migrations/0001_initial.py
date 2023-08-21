# Generated by Django 4.2.2 on 2023-08-21 13:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Morador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('data_updated', models.DateTimeField(auto_now=True)),
                ('cpf', models.CharField(max_length=14, verbose_name='CPF')),
                ('data_nascimento', models.DateField(verbose_name='Data de nascimento')),
                ('telefone_1', models.CharField(help_text='(WHATSAPP)', max_length=18, verbose_name='Telefone 1')),
                ('telefone_2', models.CharField(blank=True, max_length=18, null=True, verbose_name='Telefone 2')),
                ('cep', models.CharField(max_length=8, verbose_name='CEP')),
                ('logradouro', models.CharField(max_length=255, verbose_name='Endereço')),
                ('complemento', models.CharField(blank=True, max_length=255, null=True, verbose_name='Complemento')),
                ('longitude', models.DecimalField(decimal_places=18, help_text='Coordenada geográfica', max_digits=20, max_length=255, verbose_name='longitude')),
                ('latitude', models.DecimalField(decimal_places=18, help_text='Coordenada geográfica', max_digits=20, max_length=255, verbose_name='latitude')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.genero', verbose_name='Gênero')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.municipio', verbose_name='Município')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='morador_usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
