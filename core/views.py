from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from . import models
from . import serializers

class ClientReadAccessMixin:
    def get_permissions(self):
        self.permission_classes = [IsAdminUser]

        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]

        return super().get_permissions()

class ClientOwnedQuerysetMixin:
    def get_queryset(self):
        qs = super().get_queryset()

        if not self.request.user.is_staff:
            qs = qs.filter(client = self.request.user)
        
        return qs


class ClientListCreate(generics.ListCreateAPIView):
    queryset = models.User.objects.filter(is_staff = False)
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAdminUser]

class ProjectListCreate(
    ClientReadAccessMixin,
    ClientOwnedQuerysetMixin,
    generics.ListCreateAPIView
):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer

class PersonListCreate(generics.ListCreateAPIView):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer
    permission_classes = [IsAdminUser]

class DataPointListCreate(generics.ListCreateAPIView):
    queryset = models.DataPoint.objects.all()
    serializer_class = serializers.DataPointSerializer
    permission_classes = [IsAdminUser]

class ProjectObjectListCreate(
    ClientReadAccessMixin,
    ClientOwnedQuerysetMixin,
    generics.ListCreateAPIView
):
    queryset = models.ProjectObject.objects.all()
    serializer_class = serializers.ProjectObjectSerializer

class ClientRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.User.objects.filter(is_staff = False)
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAdminUser]

class ProjectRetrieveUpdateDestory(
    ClientReadAccessMixin,
    ClientOwnedQuerysetMixin,
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer

class PersonRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer

class DataPointRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.DataPoint.objects.all()
    serializer_class = serializers.DataPointSerializer

class ProjectObjectRetrieveUpdateDestory(
    ClientReadAccessMixin,
    ClientOwnedQuerysetMixin,
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = models.ProjectObject.objects.all()
    serializer_class = serializers.ProjectObjectSerializer
