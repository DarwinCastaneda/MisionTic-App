from rest_framework import status, views
from rest_framework.response import Response
#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from hosApp.serializers.enfermeroSerializer import EnfermeroSerializer
from hosApp.models.enfermero import Enfermero

class PacienteCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = EnfermeroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)