from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Project(models.Model):
    label = models.CharField(max_length=35)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.label


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class DataPoint(models.Model):
    label = models.CharField(max_length=35)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.label


class ProjectObject(models.Model):
    label = models.CharField(max_length=70)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="project_objects"
    )
    responsible_persons = models.ManyToManyField(Person)
    data_points = models.ManyToManyField(DataPoint)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Object"

    def __str__(self):
        return self.label


class ProjectObjectDataPoint(models.Model):
    project_object = models.ForeignKey(ProjectObject, on_delete=models.CASCADE, related_name="data_points_data")
    data_point = models.ForeignKey(DataPoint, on_delete=models.CASCADE)
    value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Object Data Point"

    def __str__(self):
        return f"Object: {self.project_object.label}, Data point: {self.data_point.label}, Value: {self.value}"
