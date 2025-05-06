from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from . import models
from . import serializers


class ClientReadAccessMixin:
    """
    Mixin to dynamically set permissions for views based on the HTTP method.

    This mixin modifies the `permission_classes` attribute to apply different
    permissions depending on whether the request method is a GET request or not.

    - For GET requests, the `IsAuthenticated` permission is applied.
    - For all other request methods, the `IsAdminUser` permission is applied.

    Methods:
        get_permissions(): Overrides the default method to dynamically set
        `permission_classes` based on the request method.
    """
    def get_permissions(self):
        self.permission_classes = [IsAdminUser]

        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated]

        return super().get_permissions()


class ClientOwnedQuerysetMixin:
    """
    A mixin to filter querysets based on the client's ownership.

    Attributes:
        client_lookup (str): The field name used to filter the queryset by client. 
                             Defaults to "client".

    Methods:
        get_queryset():
            Returns a filtered queryset. If the requesting user is not a staff 
            member or superuser, the queryset is filtered to include only objects 
            associated with the user's client.
    """
    client_lookup = "client"

    def get_queryset(self):
        qs = super().get_queryset()

        if not self.request.user.is_staff or not self.request.user.is_superuser:
            lookup = {self.client_lookup: self.request.user.client}
            qs = qs.filter(**lookup)

        return qs


class ClientListCreate(generics.ListCreateAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer
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
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer
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
