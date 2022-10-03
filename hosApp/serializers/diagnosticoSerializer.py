from rest_framework import serializers
from hosApp.models.diagnostico import Diagnostico
from hosApp.models.historia_clinica import HistoriaClinica
from hosApp.serializers.diagnosticoSerializer import DiagnosticoSerializer

class DiagnosticoSerializer(serializers.ModelSerializer):
    historiaClinica = DiagnosticoSerializer() 
    class Meta:
        model = Diagnostico
        fields = ['id_historiaClinica','sugerencia','fecha']
    def create(self, validated_data):
            historiaClinicaData = validated_data.pop('paciente') #relacionando
            diagnosticoInstance = Diagnostico.objects.create(**validated_data)  #creando instanciadelpaciente
            HistoriaClinica.objects.create(id_diagnostico=diagnosticoInstance, **historiaClinicaData) #creandoinstanciadelusuario
            return diagnosticoInstance

    def to_representation(self, obj):
        diagnostico = Diagnostico.objects.get(id_diagnostico=obj.id_diagnostico)
        historiaClinica = HistoriaClinica.objects.get(id=obj.id_historiaClinica)
        return {   
                    'historiaClinica':{    
                        'motivo_consulta': historiaClinica.motivo_consulta,
                        'enfermedad_actual': historiaClinica.enfermedad_actual,
                        'fecha_consulta': historiaClinica.fecha_consulta,
                    },   
                        'sugerencia': diagnostico.sugerencia, 
                        'fecha': diagnostico.fecha,           
        }