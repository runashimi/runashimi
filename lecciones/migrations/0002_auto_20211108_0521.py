# Generated by Django 2.2.12 on 2021-11-08 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecciones', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='rol',
        ),
        migrations.AlterField(
            model_name='rol',
            name='nombre',
            field=models.CharField(max_length=255),
        ),
    ]
