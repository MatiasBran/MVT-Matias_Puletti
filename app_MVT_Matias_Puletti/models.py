from django.db import models

# Create your models here.



class Familia(models.Model):
    nombre_familiar = models.CharField(max_length=50)
    edad_familiar = models.IntegerField()
    nacimiento_familiar = models.DateField()






























