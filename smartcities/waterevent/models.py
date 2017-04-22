from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Location(models.Model):
    locationId=models.CharField(max_length=5)
    locName=models.CharField(max_length=20)
    locLatitude=models.CharField(max_length=5)
    locLongitude=models.CharField(max_length=5)

class Event(models.Model):
    eventId=models.CharField(max_length=5,primary_key = True)
    description=models.CharField(max_length=500)
    type=models.CharField(max_length=20)
    date=models.CharField(max_length=10)
    #locationId=models.ForeignKey(Location,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("index", kwargs={'pk': self.pk})

    def __str__(self):
        return self.type

    class Meta:
        managed = False
        db_table = 'Event'
        app_label = 'event'

class ObservReport(models.Model):
    observId = models.CharField(max_length=5,primary_key = True)
    date = models.DateField(max_length=10)
    observName = models.CharField(max_length=20)
    overflow = models.BooleanField(max_length=20)

    def _get_absolute_url(self):
        return reverse("report-update",kwargs ={'pk':self.pk})

    def __str__(self):
        return self.type

    class Meta:
        managed = False
        db_table = 'ObservReport'
        app_label = 'report'

class Region(models.Model):
    regionId=models.IntegerField()
    regionName=models.CharField(max_length=20)


class Happen(models.Model):
    regionId = models.IntegerField()
    eventId = models.IntegerField()


class Sensor(models.Model):
    sensorId = models.IntegerField()
    volume = models.FloatField()
    phLevel = models.IntegerField()
    contaminantLevel = models.FloatField()
    date = models.DateField()
    observId = models.IntegerField()


class Pipe(models.Model):
    pipeId = models.IntegerField()
    capacity = models.FloatField(20)
    sourceLocation = models.IntegerField()
    endLocation = models.IntegerField()
