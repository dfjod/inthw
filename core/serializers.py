from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["id", "username"]


class ClientSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')

    class Meta:
        model = models.Client
        fields = ["username"]


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = ["id", "first_name", "last_name"]


class DataPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DataPoint
        fields = ["id", "label"]


class ProjectObjectDataPointSerializer(serializers.ModelSerializer):
    data_point_label = serializers.CharField(source="data_point.label", read_only=True)
    data_point_id = serializers.IntegerField(source="data_point.id", read_only=True)

    class Meta:
        model = models.ProjectObjectDataPoint
        fields = ["data_point_id", "data_point_label", "value", "created_at"]


class ProjectObjectSerializer(serializers.ModelSerializer):
    responsible_persons = PersonSerializer(many=True, read_only=True)
    data_points = DataPointSerializer(many=True, read_only=True)
    data_points_data = ProjectObjectDataPointSerializer(many=True, read_only=True)

    class Meta:
        model = models.ProjectObject
        fields = ["id", "label", "project", "responsible_persons", "data_points", "data_points_data"]


class ProjectSerializer(serializers.ModelSerializer):
    project_objects = ProjectObjectSerializer(many=True, read_only=True)

    class Meta:
        model = models.Project
        fields = ["id", "label", "client", "project_objects"]
