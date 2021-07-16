from django.db import models


# Create your models here.
class Patroller(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    code_name = models.CharField(max_length=255)
    armed = models.BooleanField(default=False)
    current_point = models.OneToOneField('WatchPoint', primary_key=False, on_delete=models.DO_NOTHING)
    cell = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telegram = models.CharField(max_length=255)


class Shift(models.Model):
    watch_point = models.OneToOneField('WatchPoint', on_delete=models.DO_NOTHING)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    patrollers = models.ForeignKey('Patroller', on_delete=models.DO_NOTHING)


class WatchPoint(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    alert = models.BooleanField(default=False)
    full = models.BooleanField(default=False)