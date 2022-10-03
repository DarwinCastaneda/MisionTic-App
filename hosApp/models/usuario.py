from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password
from .tipo_usuario import TipoUsuario
from .paciente import Paciente
from .familiar import Familiar
from .medico import Medico
from .enfermero import Enfermero

class UserManager(BaseUserManager):
    def create_user(self, nombre_usuario, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not nombre_usuario:
            raise ValueError('Users must have an username')
        usuario = self.model(nombre_usuario=nombre_usuario)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, nombre_usuario, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        usuario = self.create_user(
            nombre_usuario=nombre_usuario,
            password=password,
    )
        usuario.is_admin = True
        usuario.save(using=self._db)
        return usuario

class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)  
    nombre_usuario = models.CharField('Usuario', max_length = 15, unique=True)
    password = models.CharField('Password', max_length = 256)
    nombre = models.CharField('Nombre', max_length = 30)
    apellido = models.CharField('Apellido', max_length = 30)
    celular = models.CharField('Celular', max_length = 10)
    correo = models.EmailField('Correo', max_length = 30)
    genero = models.CharField('Genero', max_length = 2)
    edad = models.CharField('Edad', max_length = 2)
    id_tipoUsuario= models.ForeignKey(TipoUsuario,related_name='usuario', on_delete=models.CASCADE)
    id_enfermero= models.OneToOneField(Enfermero,related_name='usuario', on_delete=models.CASCADE)
    id_paciente= models.OneToOneField(Paciente,related_name='usuario', on_delete=models.CASCADE)
    id_familiar= models.OneToOneField(Familiar,related_name='usuario', on_delete=models.CASCADE)
    id_medico= models.OneToOneField(Medico,related_name='usuario', on_delete=models.CASCADE)



    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'nombre_usuario'