from django.db import models
from users.models import User
from datetime import datetime

# Modelo da tabela Score
class Score(models.Model):
    type_score = models.CharField('Tipo', max_length=5)
    score_description = models.TextField('Descrição', max_length=255)
    equivalent_score = models.IntegerField('Equivalência')
    
    BONUS = 'B'
    PENALTY = 'P'
    SCORE_CHOICES = [
        (BONUS, 'Bônus'),
        (PENALTY, 'Penalidade'),
    ]
    score_specification = models.CharField(verbose_name='Specification', max_length=1, choices=SCORE_CHOICES, default=BONUS)

    class Meta:
        verbose_name = 'Pontuação'
        verbose_name_plural = 'Pontuações'

    def __str__(self):
        return self.type_score

    def __add__(self, other_score):
        return self.equivalent_score + other_score.equivalent_score

# Modelo da tabela User_has_score
class User_has_score(models.Model):
    user = models.ForeignKey(User, verbose_name='Usuário', related_name='user_has_scores', on_delete=models.CASCADE)
    score = models.ForeignKey(Score, verbose_name='Pontuação', related_name='users_has_score', on_delete=models.PROTECT)
    score_comment = models.TextField('Comentário', max_length=255)
    score_date = models.DateTimeField(default=datetime.now)
    admin_username = models.CharField(verbose_name='Nome', max_length=100, default="")

    class Meta:
        verbose_name = 'Pontuação Usuário'
        verbose_name_plural = 'Pontuações Usuários'

    def __str__(self):
        return self.user.username + " - " + self.score.type_score