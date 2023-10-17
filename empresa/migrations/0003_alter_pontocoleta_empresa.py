# Generated by Django 4.2.2 on 2023-10-17 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0002_pontocoleta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontocoleta',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ponto_coleta_empresa', to='empresa.empresa'),
        ),
    ]