# Generated by Django 2.2.6 on 2019-11-06 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoremanager', '0002_auto_20191105_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='score_specification',
            field=models.CharField(choices=[('B', 'Bônus'), ('P', 'Penalidade')], default='B', max_length=1, verbose_name='Specification'),
        ),
    ]
