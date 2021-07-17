from django.db import models


# Create your models here.
class Patroller(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    code_name = models.CharField(max_length=255, null=True, blank=True)
    armed = models.BooleanField(default=False)
    current_point = models.OneToOneField('WatchPoint', primary_key=False, on_delete=models.DO_NOTHING, null=True, blank=True)
    cell = models.CharField(max_length=255)
    email = models.CharField(max_length=255, null=True, blank=True)
    telegram = models.CharField(max_length=255, null=True, blank=True)
    preferred_shifts = models.ManyToManyField('Shift', related_name='patroller_pref_shift', null=True, blank=True)
    preferred_watchpoint = models.ManyToManyField('WatchPoint', related_name='patroller_pref_point', null=True, blank=True)

    def __str__(self):
        if self.code_name is not None and self.code_name != '':
            return self.code_name
        else:
            return '{} {}'.format(self.first_name, self.last_name)


class Shift(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        string_time = self.start_time.strftime("%H:%M") + " - " + self.end_time.strftime("%H:%M")
        return string_time


class Team(models.Model):
    watch_point = models.ForeignKey('WatchPoint', on_delete=models.DO_NOTHING)
    patrollers = models.ManyToManyField('Patroller', null=True, blank=True)
    shift = models.ForeignKey('Shift', on_delete=models.DO_NOTHING)
    day = models.DateField()


class WatchPoint(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    link = models.CharField(max_length=255, null=True, blank=True)
    alert = models.BooleanField(default=False)
    full = models.BooleanField(default=False)
    abbreviation = models.CharField(max_length=5, default=None, null=True)

    def __str__(self):
        return self.name
