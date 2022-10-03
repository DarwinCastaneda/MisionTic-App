from django.db import models

class Enfermero (models.Model):
    id_enfermero= models.AutoField(primary_key=True)
    especialidad= models.CharField(max_length=10)