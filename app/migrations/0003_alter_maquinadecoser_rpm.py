# Generated by Django 4.2.3 on 2024-05-17 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_fichatecnica_rpm_alter_maquinadecoser_rpm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maquinadecoser',
            name='rpm',
            field=models.IntegerField(),
        ),
    ]
