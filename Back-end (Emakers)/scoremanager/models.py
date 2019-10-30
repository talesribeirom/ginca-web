from django.db import models
from users.models import User


class Score(models.Model):
    type_score = models.CharField('Tipo', max_length=5)
    score_description = models.TextField('Descrição', max_length=255)
    equivalent_score = models.IntegerField('Equivalência')

    class Meta:
        verbose_name = 'Pontuação'
        verbose_name_plural = 'Pontuações'

    def __str__(self):
        return self.type_score

class User_has_score(models.Model):
    user_name = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.CASCADE)
    user_score = models.ForeignKey(Score, verbose_name='Pontuação', on_delete=models.PROTECT)
    score_comment = models.TextField('Comentário', max_length=255)

    class Meta:
        verbose_name = 'Pontuação Usuário'
        verbose_name_plural = 'Pontuações Usuários'

    def __str__(self):
        return self.score_comment
