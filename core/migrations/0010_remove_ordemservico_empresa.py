# Generated by Django 4.2.2 on 2023-10-19 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_itemservico_ponto_coleta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordemservico',
            name='empresa',
        ),
    ]
