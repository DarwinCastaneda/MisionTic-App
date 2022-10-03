from rest_framework import serializers
from hosApp.models.usuario import Usuario
from hosApp.models.enfermero import Enfermero

from hosApp.serializers.usuarioSerializer import UsuarioSerializer


class EnfermeroSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = Enfermero
        fields = []

        def create(self, validated_data):
            usuarioData = validated_data.pop('usuario')  # relacionando
            enfermeroInstance = Enfermero.objects.create(**validated_data)  # creando instanciadelpaciente
                
           
            Usuario.objects.create(id_paciente=enfermeroInstance, **usuarioData)
            return enfermeroInstance

    def to_representation(self, obj):
        enfermero = Enfermero.objects.get(id_enfermero=obj.id)
        usuario = Usuario.objects.get(id_enfermero=obj.id)
        return {
            'especializacion': enfermero.especializacion,
            'usuario': {
                'nombre': usuario.nombre,
                'apellido': usuario.apellido,
                'celular': usuario.celular,
                'correo': usuario.correo,
                'genero': usuario.genero,
                'edad': usuario.edad,
            }
        }
