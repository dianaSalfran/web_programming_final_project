# Generated by Django 4.1.3 on 2023-01-13 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto_final', '0006_artista_id_alter_artista_ci'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='ci',
            field=models.IntegerField(),
        ),
    ]
