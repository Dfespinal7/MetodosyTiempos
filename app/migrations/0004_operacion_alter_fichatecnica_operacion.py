# Generated by Django 4.2.3 on 2024-05-21 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_maquinadecoser_rpm'),
    ]

    operations = [
        migrations.CreateModel(
            name='operacion',
            fields=[
                ('codigo', models.CharField(blank=True, max_length=150, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='fichatecnica',
            name='operacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.operacion'),
        ),
    ]
