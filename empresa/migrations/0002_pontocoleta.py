# Generated by Django 4.2.2 on 2023-10-15 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_statusitem'),
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PontoColeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.DecimalField(decimal_places=18, help_text='Coordenada geográfica do ponto de coleta', max_digits=20, max_length=255, verbose_name='longitude')),
                ('latitude', models.DecimalField(decimal_places=18, help_text='Coordenada geográfica do ponto de coleta', max_digits=20, max_length=255, verbose_name='latitude')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='empresa.empresa')),
                ('tipo_aceito', models.ManyToManyField(to='core.tipo', verbose_name='Tipos de Itens Aceitos')),
            ],
        ),
    ]
