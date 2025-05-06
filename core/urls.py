from django.urls import path
from . import views

urlpatterns = [
    path("v1/clients/", views.ClientListCreate.as_view(), name="client_view_create"),
    path("v1/projects/", views.ProjectListCreate.as_view(), name="project_view_create"),
    path("v1/persons/", views.PersonListCreate.as_view(), name="person_view_create"),
    path("v1/datapoints/", views.DataPointListCreate.as_view(), name="datapoint_view_create"),
    path("v1/objects/", views.ProjectObjectListCreate.as_view(), name="object_view_create"),
    path("v1/clients/<int:pk>/", views.ClientRetrieveUpdateDestroy.as_view(), name="client_view_retrieve_udpate_destroy"),
    path("v1/projects/<int:pk>/", views.ProjectRetrieveUpdateDestory.as_view(), name="project_view_retrieve_udpate_destroy"),
    path("v1/persons/<int:pk>/", views.PersonRetrieveUpdateDestory.as_view(), name="person_view_retrieve_udpate_destroy"),
    path("v1/datapoints/<int:pk>/", views.DataPointRetrieveUpdateDestory.as_view(), name="datapoint_view_retrieve_udpate_destroy"),
    path("v1/objects/<int:pk>/", views.ProjectObjectRetrieveUpdateDestory.as_view(), name="object_view_retrieve_udpate_destroy"),
]
