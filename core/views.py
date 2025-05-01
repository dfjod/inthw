from django.shortcuts import render
from rest_framework import generics
from . import models
from . import serializers

class ClientListCreate(generics.ListCreateAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer

class ProjectListCreate(generics.ListCreateAPIView):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer

class PersonListCreate(generics.ListCreateAPIView):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer

class DataPointListCreate(generics.ListCreateAPIView):
    queryset = models.DataPoint.objects.all()
    serializer_class = serializers.DataPointSerializer

class ObjectListCreate(generics.ListCreateAPIView):
    queryset = models.Object.objects.all()
    serializer_class = serializers.ObjectSerializer

class ClientRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer
    lookup_field = 'pk'

class ProjectRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    lookup_field = 'pk'

class PersonRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer
    lookup_field = 'pk'

class DataPointRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.DataPoint.objects.all()
    serializer_class = serializers.DataPointSerializer
    lookup_field = 'pk'

class ObjectRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Object.objects.all()
    serializer_class = serializers.ObjectSerializer
    lookup_field = 'pk'
