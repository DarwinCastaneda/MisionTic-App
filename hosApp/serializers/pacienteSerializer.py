from rest_framework import serializers
from hosApp.models.usuario import Usuario
from hosApp.models.paciente import Paciente
from .usuarioSerializer import UsuarioSerializer

class PacienteSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer() 
    class Meta:
        model = Paciente
        fields = ['usuario','direccion','ciudad','fecha_nacimiento']
    def create(self, validated_data):
            usuarioData = validated_data.pop('usuario') #relacionando
            pacienteInstance = Paciente.objects.create(**validated_data)  #creando instanciadelpaciente
            Usuario.objects.create(id_paciente=pacienteInstance, **usuarioData) #creandoinstanciadelusuario
            return pacienteInstance

    def to_representation(self, obj):
        paciente = Paciente.objects.get(id_paciente=obj.id)
        usuario = Usuario.objects.get(id=obj.id)
        return {      
                    'direccion': paciente.direccion,
                    'ciudad': paciente.ciudad,
                    'fecha_nacimiento': paciente.fecha_nacimiento,
                    'usurio':{
                        'nombre': usuario.nombre,
                        'apellido': usuario.apellido,
                        'celular': usuario.celular,
                        'genero': usuario.genero,
                    }
            }
           