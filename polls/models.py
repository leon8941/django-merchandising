import datetime
import pandas as pd

from django.db import models
from django.utils import timezone
from django_google_maps import fields as map_fields

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class GeolocationData(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.CharField(max_length=50)
    customer_code = models.CharField(max_length=100)
    customer_short_name = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return "{}".format(self.id)


