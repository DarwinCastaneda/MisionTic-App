from django.db import models


class HistoriaClinica(models.Model):
    id_historiaClinica=models.AutoField(primary_key=True)
    motivo_consulta= models.CharField(max_length=100)
    enfermedad_actual=models.CharField(max_length=100)
    fecha_consulta= models.DateField()