from django.db import models

class Pontuacao(models.Model):
    descricaoPontuacao = models.TextField('Descrição', max_length=255)
    pontosEquivalentes = models.IntegerField()

    class Meta:
        verbose_name = 'Pontuação'
        verbose_name_plural = 'Pontuações'
    
    def __str__(self):
        return descricaoPontuacao

class Usuario(models.Model):
    nomeUsuario = models.CharField('Nome', max_length=255)
    emailUsuario = models.CharField('Email', max_length=255)
    sexoUsuario = models.CharField('Sexo', max_length=1)
    pontuacoes = models.ForeignKey(Pontuacao, on_delete=models.CASCADE)

    def __str__(self):
        return nomeUsuario

class Login(models.Model):
    nomeUsuario = models.CharField('Usuário', max_length=100)
    senhaUsuario = models.CharField('Senha', max_length=100)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Usuario_possui_pontuacao(models.Model):
    nomeUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pontuacaoUsuario = models.ForeignKey(Pontuacao, on_delete=models.PROTECT)
    comentarioPontuacao = models.TextField('Comentario', max_length=255)

class Ranking(models.Model):
    pontuacaoTotal = models.IntegerField(default=0)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)