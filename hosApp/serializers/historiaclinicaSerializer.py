from rest_framework import serializers
from hosApp.models.paciente import Paciente
from hosApp.models.historia_clinica import HistoriaClinica
from hosApp.serializers.pacienteSerializer import PacienteSerializer

class HistoriaClinicaSerializer(serializers.ModelSerializer):
    Paciente = PacienteSerializer() 
    class Meta:
        model = HistoriaClinica
        fields = ['id_paciente','motivo_consulta','enfermedad_actual','fecha_consulta']
    def create(self, validated_data):
            pacienteData = validated_data.pop('paciente') #relacionando
            historiaClinicaInstance = HistoriaClinica.objects.create(**validated_data)  #creando instanciadelpaciente
            Paciente.objects.create(id_paciente=historiaClinicaInstance, **pacienteData) #creandoinstanciadelusuario
            return historiaClinicaInstance

    def to_representation(self, obj):
        historiaClinica = HistoriaClinica.objects.get(id_historiaClinica=obj.id_historiaClinica)
        paciente = Paciente.objects.get(id=obj.paciente)
        return {   
                    'paciente':{    
                        'direccion': paciente.direccion,
                        'ciudad': paciente.ciudad,
                        'fecha_nacimiento': paciente.fecha_nacimiento,
                    },   
                        'motivo_consulta': historiaClinica.motivo_consulta, 
                        'enfermedad_actual': historiaClinica.enfermedad_actual,
                        'fecha_consulta': historiaClinica.fecha_consulta,  
            
                }