# Generated by Django 3.2.4 on 2021-06-11 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parroquia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre Parroquia')),
                ('tipo_parroquia', models.CharField(choices=[('urbana', 'Urbana '), ('rural', 'Rural')], max_length=30, verbose_name='Ubicación de Parroquia')),
            ],
        ),
        migrations.CreateModel(
            name='Ciudadela',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre Ciudadela')),
                ('num_viviendas', models.IntegerField(verbose_name='Número de viviendas')),
                ('num_edificios', models.IntegerField(verbose_name='Número de edificios')),
                ('num_parques', models.CharField(choices=[('1', 'Parque 1'), ('2', 'Parque 2'), ('3', 'Parque 3'), ('4', 'Parque 4'), ('5', 'Parque 5'), ('6', 'Parque 6')], max_length=30, verbose_name='Numero de Parques')),
                ('parroquia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Parroquia', to='ordenamiento.parroquia')),
            ],
        ),
    ]