# Generated by Django 2.2.5 on 2019-10-15 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pontuacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricaoPontuacao', models.TextField(max_length=255, verbose_name='Descrição')),
                ('pontosEquivalentes', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Pontuação',
                'verbose_name_plural': 'Pontuações',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeUsuario', models.CharField(max_length=255, verbose_name='Nome')),
                ('emailUsuario', models.CharField(max_length=255, verbose_name='Email')),
                ('sexoUsuario', models.CharField(max_length=1, verbose_name='Sexo')),
                ('pontuacoes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Pontuacao')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_possui_pontuacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentarioPontuacao', models.TextField(max_length=255, verbose_name='Comentario')),
                ('nomeUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Usuario')),
                ('pontuacaoUsuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Pontuacao')),
            ],
        ),
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pontuacaoTotal', models.IntegerField(default=0)),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeUsuario', models.CharField(max_length=100, verbose_name='Usuário')),
                ('senhaUsuario', models.CharField(max_length=100, verbose_name='Senha')),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Usuario')),
            ],
        ),
    ]
