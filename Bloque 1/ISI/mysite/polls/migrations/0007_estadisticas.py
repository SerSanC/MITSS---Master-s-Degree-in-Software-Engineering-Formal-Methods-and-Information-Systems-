# Generated by Django 3.0.2 on 2020-01-06 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_alquileres'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estadisticas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_de_creacion', models.DateField(max_length=25)),
                ('total_gastado', models.FloatField()),
            ],
        ),
    ]
