from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Location(models.Model):
    locationId=models.CharField(max_length=5)
    locName=models.CharField(max_length=20)
    locLatitude=models.CharField(max_length=5)
    locLongitude=models.CharField(max_length=5)

class Event(models.Model):
    eventId=models.CharField(max_length=5)
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