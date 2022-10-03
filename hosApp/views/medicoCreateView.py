from rest_framework import status, views
from rest_framework.response import Response
#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from hosApp.serializers.medicoSerializer import MedicoSerializer
from hosApp.models.medico import Medico

class PacienteCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = MedicoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)