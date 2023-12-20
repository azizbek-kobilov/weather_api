from django.db import models
from model_utils.models import TimeStampedModel


class WeatherData(TimeStampedModel):
    city = models.CharField(max_length=255)
    data = models.JSONField()

    class Meta:
        ordering = ['-modified']

    def __str__(self):
        return str(self.city) + ' - ' + str(self.created)
