from django.db import models
from django.contrib.auth.models import User


SKILL_LEVELS = (
    (1, 'Fundamental Awareness'),
    (2, 'Novice'),
    (3, 'Intermediate'),
    (4, 'Advanced'),
    (5, 'Expert'),
)


class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.CharField(max_length=100)
    skill_level = models.IntegerField(
        choices=SKILL_LEVELS,
        default=1
        )
