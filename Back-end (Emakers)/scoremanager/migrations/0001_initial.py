# Generated by Django 2.2.5 on 2019-10-24 03:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_score', models.CharField(max_length=5, verbose_name='Tipo')),
                ('score_description', models.TextField(max_length=255, verbose_name='Descrição')),
                ('equivalent_score', models.IntegerField(verbose_name='Equivalência')),
            ],
            options={
                'verbose_name': 'Pontuação',
                'verbose_name_plural': 'Pontuações',
            },
        ),
        migrations.CreateModel(
            name='User_has_score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_comment', models.TextField(max_length=255, verbose_name='Comentário')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_score', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='scoremanager.Score')),
            ],
        ),
    ]
