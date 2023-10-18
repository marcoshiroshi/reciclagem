# Generated by Django 4.2.2 on 2023-10-18 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0003_alter_pontocoleta_empresa'),
        ('core', '0008_alter_itemservico_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemservico',
            name='ponto_coleta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='itens_ponto_coleta', to='empresa.pontocoleta'),
        ),
    ]