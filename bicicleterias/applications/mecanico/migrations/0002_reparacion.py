# Generated by Django 4.0.3 on 2022-04-07 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
        ('mecanico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='reparacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.ManyToManyField(to='clientes.clientes')),
                ('mecanico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mecanico.mecanico')),
            ],
        ),
    ]
