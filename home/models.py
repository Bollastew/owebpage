from django.db import models


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
