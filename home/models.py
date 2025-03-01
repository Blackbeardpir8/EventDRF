from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Event(models.models):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    capacity = models.IntegerField()
    ticket_price = models.FloatField(default = 250)
    status = models.CharField(max_length=255,default=(('Upcoming','Upcoming'),('Cancled','Cancled'),('Happning','Happning')))

