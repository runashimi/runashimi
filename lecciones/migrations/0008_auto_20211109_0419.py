# Generated by Django 2.2.12 on 2021-11-09 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lecciones', '0007_auto_20211109_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preguntarespondida',
            name='respuesta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='lecciones.ElegirRespuesta'),
            preserve_default=False,
        ),
    ]
