# Generated by Django 5.0.6 on 2024-05-30 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_codigos_gsd_formulariodinamico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulariodinamico',
            name='tmu',
            field=models.IntegerField(),
        ),
    ]