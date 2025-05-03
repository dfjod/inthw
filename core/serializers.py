from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'username']

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = ['id', 'first_name', 'last_name']

class DataPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DataPoint
        fields = ['id', 'label']

class ProjectObjectSerializer(serializers.ModelSerializer):
    responsible_persons = PersonSerializer(many=True, read_only=True)
    data_points = DataPointSerializer(many=True, read_only=True)

    class Meta:
        model = models.ProjectObject
        fields = ['id', 'label', 'project', 'responsible_persons', 'data_points']

class ProjectSerializer(serializers.ModelSerializer):
    project_objects = ProjectObjectSerializer(many=True, read_only=True)

    class Meta:
        model = models.Project
        fields = ['id', 'label', 'client', 'project_objects']
