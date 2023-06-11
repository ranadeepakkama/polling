from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Polling(models.Model):
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=80)
    option2 = models.CharField(max_length=80)
    option3 = models.CharField(max_length=80)
    option1_count = models.IntegerField(default=0)
    option2_count = models.IntegerField(default=0)
    option3_count = models.IntegerField(default=0)
    total_result = models.IntegerField(default=0)
    voters = models.ManyToManyField(User, blank=True)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.question


