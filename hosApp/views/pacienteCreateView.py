from rest_framework import status, views
from rest_framework.response import Response
#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from hosApp.serializers.pacienteSerializer import PacienteSerializer
from hosApp.models.paciente import Paciente

class PacienteCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = PacienteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)

    """    def post(self, request, *args, **kwargs):
	serializer = UserSerializer(data=request.data)
	serializer.is_valid(raise_exception=True)
	serializer.save()

	return Response(status=status.HTTP_201_CREATED)"""