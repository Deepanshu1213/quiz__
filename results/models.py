from django.db import models
from quizes.models import Quiz
from django.contrib.auth.models import User

# Create your models here.
class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='result')
    score =models.FloatField()
    

    def __str__(self):
        return f"{self.user} scored {self.score} in {self.quiz.name}"    