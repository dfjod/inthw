from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser, models.Model):
    pass

class Project(models.Model):
    label = models.CharField(max_length=35)
    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'is_staff': False}
    )

    def __str__(self):
        return self.label

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class DataPoint(models.Model):
    label = models.CharField(max_length=35)

    def __str__(self):
        return self.label

class Object(models.Model):
    label = models.CharField(max_length=70)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    responsible_persons = models.ManyToManyField(Person)
    data_points = models.ManyToManyField(DataPoint)

    def __str__(self):
        return f'Project: {self.project}, Label: {self.label}, Responsible persons: {self.responsible_persons}, Data points: {self.data_points}'
