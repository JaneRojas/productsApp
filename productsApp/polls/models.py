from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    tittle = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    creation_date = models.DateTimeField('date published')

