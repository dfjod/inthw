from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'username']

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
