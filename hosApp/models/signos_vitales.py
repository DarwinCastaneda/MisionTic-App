from django.db import models
from .historia_clinica import HistoriaClinica

class SignosVitales(models.Model):
    id_signos_vitales= models.AutoField(primary_key=True)
    oximetria= models.CharField(max_length=20)
    frecuencia_respiratoria= models.CharField(max_length=20)
    frecuencia_cardiaca= models.CharField(max_length=20)
    temperatura= models.CharField(max_length=10)
    presion_arterial= models.CharField(max_length=20)
    glicemias= models.CharField(max_length=20)
    fecha_hora= models.DateTimeField()
    id_historiaClinica= models.ForeignKey(HistoriaClinica,related_name='signos',on_delete=models.CASCADE)