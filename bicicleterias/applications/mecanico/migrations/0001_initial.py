# Generated by Django 4.0.3 on 2022-04-07 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mecanico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=40)),
                ('cedula', models.CharField(max_length=40)),
                ('telefono', models.IntegerField()),
            ],
        ),
    ]
