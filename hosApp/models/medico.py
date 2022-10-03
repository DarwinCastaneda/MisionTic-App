from django.db import models


class Medico(models.Model):
    id_medico= models.AutoField(primary_key=True)
    tarjeta_profesional= models.CharField(max_length=20)
    especialidad= models.CharField(max_length=20)