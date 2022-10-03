from django.db import models

class TipoUsuario(models.Model):
    id_tipoUsuario= models.AutoField(primary_key=True)
    rol= models.CharField(max_length=10)