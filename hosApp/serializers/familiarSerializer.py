from rest_framework import serializers
from hosApp.models.usuario import Usuario
from hosApp.models.familiar import Familiar

from hosApp.serializers.usuarioSerializer import UsuarioSerializer

class FamiliarSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer() 
    class Meta:
        model = Familiar
        fields = []
        def create(self, validated_data):
            usuarioData = validated_data.pop('usuario') #relacionando
            familiarInstance = Familiar.objects.create(**validated_data)  #creando instanciadelpaciente
            Usuario.objects.create(id_paciente=familiarInstance, **usuarioData) #creandoinstanciadelusuario
            return familiarInstance

    def to_representation(self, obj):
        familiar = Familiar.objects.get(id_familiar=obj.id)
        usuario = Usuario.objects.get(id_familiar=obj.id)
        return {
                    'usuario': {
                        'nombre': usuario.nombre,
                        'apellido': usuario.apellido,
                        'celular': usuario.celular,
                        'correo': usuario.correo,
                        'genero': usuario.genero,
                        'edad': usuario.edad,
                         },
                        'eps': familiar.eps,
                        'grupo_sanguineo': familiar.grupo_sanguineo,
                        'parentezco': familiar.parentezco,
                            
                }

    