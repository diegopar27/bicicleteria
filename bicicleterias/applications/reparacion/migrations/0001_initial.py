# Generated by Django 4.0.3 on 2022-04-07 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
        ('mecanico', '0003_delete_reparacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reparacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_cicla', models.CharField(max_length=30)),
                ('cliente', models.ManyToManyField(to='clientes.clientes')),
                ('mecanico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mecanico.mecanico')),
            ],
        ),
    ]
