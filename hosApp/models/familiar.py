from django.db import models
from .paciente import Paciente


class Familiar(models.Model):
    id_familar=models.AutoField(primary_key=True)
    correo = models.EmailField(max_length=35)
    parentesco= models.CharField(max_length=10)
    id_paciente= models.OneToOneField(Paciente,related_name='enfermero',on_delete=models.CASCADE)