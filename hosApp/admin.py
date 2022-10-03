from django.contrib import admin

# Register your models here.
from .models.usuario import Usuario
from .models.diagnostico import Diagnostico
from .models.enfermero import Enfermero
from .models.familiar import Familiar
from .models.historia_clinica import HistoriaClinica
from .models.medico import Medico
from .models.paciente import Paciente
from .models.signos_vitales import SignosVitales
from .models.tipo_usuario import TipoUsuario


admin.site.register(Usuario)
admin.site.register(Diagnostico)
admin.site.register(Familiar)
admin.site.register(Enfermero)
admin.site.register(HistoriaClinica)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(SignosVitales)
admin.site.register(TipoUsuario)