from rest_framework import serializers
from .models import HealthProgram, Client

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthProgram
        fields = ['id', 'name']

class ClientSerializer(serializers.ModelSerializer):
    programs = ProgramSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'name', 'age', 'programs']

class ClientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'age']
