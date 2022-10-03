from django.db import models
from .historia_clinica import HistoriaClinica


class Diagnostico (models.Model):
    id_diagnostico= models.AutoField(primary_key=True)
    sugerencia= models.TextField()
    fecha= models.DateTimeField()
    id_historiaClinica= models.ForeignKey(HistoriaClinica,related_name='diagnostico',on_delete=models.CASCADE)

