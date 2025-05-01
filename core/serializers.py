from rest_framework import serializers
from . import models

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = ['id', 'name']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = ['id', 'label', 'client']

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = ['id', 'first_name', 'last_name']

class DataPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DataPoint
        fields = ['id', 'label']

class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Object
        fields = ['id', 'label', 'project', 'responsible_persons', 'data_points']
