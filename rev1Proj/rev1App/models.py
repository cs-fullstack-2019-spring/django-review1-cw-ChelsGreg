from django.db import models

# Create your models here.

class Cocktails(models.Model):
    name = models.CharField(max_length=100)
    alcPercent = models.IntegerField(default=0)
    serveGlass = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'