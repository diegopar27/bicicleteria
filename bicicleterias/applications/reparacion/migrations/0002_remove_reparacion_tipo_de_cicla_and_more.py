# Generated by Django 4.0.3 on 2022-04-08 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipos', '0001_initial'),
        ('reparacion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reparacion',
            name='tipo_de_cicla',
        ),
        migrations.AddField(
            model_name='reparacion',
            name='tipo_de_cicla',
            field=models.ManyToManyField(to='tipos.tipos_de_bicicletas'),
        ),
    ]
