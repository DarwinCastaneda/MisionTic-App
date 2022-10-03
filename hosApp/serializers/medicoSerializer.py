from rest_framework import serializers
from hosApp.models.usuario import Usuario
from hosApp.models.medico import Medico

from hosApp.serializers.usuarioSerializer import UsuarioSerializer

class MedicoSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer() 
    class Meta:
        model = Medico
        fields = []
        def create(self, validated_data):
            usuarioData = validated_data.pop('usuario') #relacionando
            medicoInstance = Medico.objects.create(**validated_data)  #creando instanciadelpaciente
            Usuario.objects.create(id_medico=medicoInstance, **usuarioData) #creandoinstanciadelusuario
            return medicoInstance

    def to_representation(self, obj):
        medico = Medico.objects.get(id_medico=obj.id)#atributo de busqueda
        usuario = Usuario.objects.get(id_medico=obj.id)
        return {
            'especialidad': medico.especialidad,
            'tarjetaProfesional': medico.tarjeta_profesional,
            'usuario': {
                'nombre': usuario.nombre,
                'apellido': usuario.apellido,
                'celular': usuario.celular,
                'correo': usuario.correo,
                'genero': usuario.genero,
                'edad': usuario.edad,
            }
        }

    