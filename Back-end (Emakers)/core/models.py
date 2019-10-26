from django.db import models
from users.models import User


class Ranking(models.Model):
    total_score = models.IntegerField(default=0)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)