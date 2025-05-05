from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from . import models
from . import serializers


class ClientReadAccessMixin:
    def get_permissions(self):
        self.permission_classes = [IsAdminUser]

        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated]

        return super().get_permissions()


class ClientOwnedQuerysetMixin:
    client_lookup = "client"

    def get_queryset(self):
        qs = super().get_queryset()

        if not self.request.user.is_staff or not self.request.user.is_superuser:
            lookup = {self.client_lookup: self.request.user.client}
            qs = qs.filter(**lookup)

        return qs


class ClientListCreate(generics.ListCreateAPIView):
    queryset = models.User.objects.filter(is_staff=False, is_superuser=False)
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAdminUser]


class ProjectListCreate(
    ClientReadAccessMixin, ClientOwnedQuerysetMixin, generics.ListCreateAPIView
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
    ClientReadAccessMixin, ClientOwnedQuerysetMixin, generics.ListCreateAPIView
):
    queryset = models.ProjectObject.objects.all()
    serializer_class = serializers.ProjectObjectSerializer
    client_lookup = "project__client"


class ClientRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.User.objects.filter(is_staff=False)
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAdminUser]


class ProjectRetrieveUpdateDestory(
    ClientReadAccessMixin,
    ClientOwnedQuerysetMixin,
    generics.RetrieveUpdateDestroyAPIView,
):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    permission_classes = [IsAdminUser]


class PersonRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer
    permission_classes = [IsAdminUser]


class DataPointRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.DataPoint.objects.all()
    serializer_class = serializers.DataPointSerializer
    permission_classes = [IsAdminUser]


class ProjectObjectRetrieveUpdateDestory(
    ClientReadAccessMixin,
    ClientOwnedQuerysetMixin,
    generics.RetrieveUpdateDestroyAPIView,
):
    queryset = models.ProjectObject.objects.all()
    serializer_class = serializers.ProjectObjectSerializer
    permission_classes = [IsAdminUser]
    client_lookup = "project__client"
