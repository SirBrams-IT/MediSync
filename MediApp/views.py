from rest_framework import generics
from .models import Client, HealthProgram
from .serializers import ClientSerializer, ProgramSerializer, ClientCreateSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.urls import reverse


class ProgramCreateView(generics.CreateAPIView):
    queryset = HealthProgram.objects.all()
    serializer_class = ProgramSerializer

    def create(self, request, *args, **kwargs):
        program_name = request.data.get('name')

        if HealthProgram.objects.filter(name=program_name).exists():
            return Response({
                "success": False,
                "message": f"Program '{program_name}' already exists."
            }, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

class ClientCreateView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientCreateSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            "success": True,
            "message": "Client registered successfully!",
            "next_step": reverse('enroll-client')  # URL to enroll client
        }, status=status.HTTP_201_CREATED)

class ClientListView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


@api_view(['POST'])
def enroll_client(request):
    client_id = request.data.get('client_id')
    program_name = request.data.get('program_name')

    try:
        client = Client.objects.get(id=client_id)
        program = HealthProgram.objects.get(name=program_name)  # Query by unique program name

        # Check if the client is already enrolled in this program
        if program in client.programs.all():
            return Response({
                "success": False,
                "message": "Client is already enrolled in this program."
            }, status=status.HTTP_400_BAD_REQUEST)

        # Enroll client in the program
        client.programs.add(program)

        return Response({
            "success": True,
            "message": "Client enrolled in program successfully!"
        }, status=status.HTTP_200_OK)

    except Client.DoesNotExist:
        return Response({
            "success": False,
            "message": "Client not found."
        }, status=status.HTTP_404_NOT_FOUND)
    except HealthProgram.DoesNotExist:
        return Response({
            "success": False,
            "message": "Program not found."
        }, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def search_client(request, name):
    try:
        client = Client.objects.get(name__iexact=name)
        serializer = ClientSerializer(client)
        return Response({
            "success": True,
            "data": serializer.data,
            "next_step": reverse('client-profile', kwargs={"id": client.id})  # Next: view full profile
        }, status=status.HTTP_200_OK)
    except Client.DoesNotExist:
        return Response({
            "success": False,
            "message": "Client not found."
        }, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def client_profile(request, id):
    try:
        client = Client.objects.get(id=id)
        serializer = ClientSerializer(client)
        return Response({
            "success": True,
            "message": "Client profile retrieved successfully.",
            "profile": serializer.data
        }, status=status.HTTP_200_OK)
    except Client.DoesNotExist:
        return Response({
            "success": False,
            "message": "Client not found."
        }, status=status.HTTP_404_NOT_FOUND)
