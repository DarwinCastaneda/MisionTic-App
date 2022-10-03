from rest_framework import serializers
from hosApp.models.historia_clinica import HistoriaClinica
from hosApp.models.signos_vitales import SignosVitales
from .signosvitalesSerializer import SignosVitales

class SignosVitalesSerializer(serializers.ModelSerializer):
    historiaClinica = HistoriaClinica() 
    class Meta:
        model = SignosVitales
        fields = ['oximetria','frecuencia_respiratoria','frecuencia_cardiaca',
        'temperatura','presion_arterial','glicemias','fecha_hora']

        def create(self, validated_data):
                historiaClinicaData = validated_data.pop('historia_clinica') #relacionando
                signosvitalesInstance = SignosVitales.objects.create(**validated_data)  #creando instanciadelpaciente
                HistoriaClinica.objects.create(id_historiaClinicaDataciente=signosvitalesInstance, **historiaClinicaData) #creandoinstanciadelusuario
                return signosvitalesInstance

    def to_representation(self, obj):
        signosVitales = SignosVitales.objects.get(id_signos_vitales=obj.signos_vitales)
        historiaClinica = HistoriaClinica.objects.get(id_historiaClinica=obj.historia_clinica)
        return {      
            'historiaClinica':{    
                'motivo_consulta': historiaClinica.motivo_consulta,
                'enfermedad_actual': historiaClinica.enfermedad_actual,
                'fecha_consulta': historiaClinica.fecha_consulta,
                },
                'oximetria': signosVitales.direccion,
                'frecuencia_respiratoria': signosVitales.ciudad,
                'frecuencia_cardiaca': signosVitales.fecha_nacimiento,
                'temperatura': signosVitales.fecha_nacimiento,
                'presion_arterial': signosVitales.fecha_nacimiento,
                'glicemias': signosVitales.fecha_nacimiento,
                'fecha_hora': signosVitales.fecha_nacimiento,

            }