from typing import Any
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    def __str__(self):
        return  "{}-{}".format(self.text , self.date)

class Entrance(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    def __str__(self):
        return  "{}-{}".format(self.text , self.date)
