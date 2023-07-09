# Generated by Django 4.2.2 on 2023-06-24 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('equipo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Inspector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('interaccion', models.TextField()),
                ('puntaje', models.DecimalField(decimal_places=2, max_digits=5)),
                ('agente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluation.agente')),
                ('inspector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluation.inspector')),
            ],
        ),
    ]