from django.db import models
from .historia_clinica import HistoriaClinica
from .medico import Medico
from .enfermero import Enfermero

class Paciente(models.Model):
    id_paciente=models.AutoField(primary_key=True)
    direccion= models.CharField(max_length=15)
    ciudad= models.CharField(max_length=35)
    fecha_nacimiento=models.DateTimeField()
    id_enfermero= models.ForeignKey(Enfermero,related_name='paciente', on_delete=models.CASCADE)
    id_historiaClinica= models.OneToOneField(HistoriaClinica,related_name='paciente', on_delete=models.CASCADE)
    id_medico= models.ForeignKey(Medico,related_name='paciente', on_delete=models.CASCADE)