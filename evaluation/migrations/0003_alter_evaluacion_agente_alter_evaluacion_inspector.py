# Generated by Django 4.2.2 on 2023-07-08 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0002_evaluacion_pregunta1_evaluacion_pregunta2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluacion',
            name='agente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='evaluaciones', to='evaluation.agente'),
        ),
        migrations.AlterField(
            model_name='evaluacion',
            name='inspector',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='evaluaciones', to='evaluation.inspector'),
        ),
    ]
