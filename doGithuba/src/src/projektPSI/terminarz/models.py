from django.db import models

class Wydarzenie(models.Model):
    cosiedzieje = models.CharField(max_length=200)
    data = models.CharField(max_length=12)

    def __unicode__(self):
        return self.data
