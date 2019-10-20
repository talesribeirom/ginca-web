from django.db import models
from users.models import User


class Score(models.Model):
    score_description = models.TextField('Descrição', max_length=255)
    # Implementar pontos equivalentes

    class Meta:
        verbose_name = 'Pontuação'
        verbose_name_plural = 'Pontuações'

    def __str__(self):
        return self.score_description

class User_has_score(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    user_score = models.ForeignKey(Score, on_delete=models.PROTECT)
    score_comment = models.TextField('Comentário', max_length=255)

class Ranking(models.Model):
    total_score = models.IntegerField(default=0)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)