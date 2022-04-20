# Generated by Django 3.2 on 2022-04-18 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
        ('reparacion', '0005_auto_20220418_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reparacion',
            name='cliente',
        ),
        migrations.AddField(
            model_name='reparacion',
            name='cliente',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='clientes.clientes'),
            preserve_default=False,
        ),
    ]