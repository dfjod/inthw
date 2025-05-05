from django.urls import path
from . import views

urlpatterns = [
    path("clients/", views.ClientListCreate.as_view(), name="client_view_create"),
    path("projects/", views.ProjectListCreate.as_view(), name="project_view_create"),
    path("persons/", views.PersonListCreate.as_view(), name="person_view_create"),
    path("datapoints/", views.DataPointListCreate.as_view(), name="datapoint_view_create"),
    path("objects/", views.ProjectObjectListCreate.as_view(), name="object_view_create"),
    path("clients/<int:pk>/", views.ClientRetrieveUpdateDestroy.as_view(), name="client_view_retrieve_udpate_destroy"),
    path("projects/<int:pk>/", views.ProjectRetrieveUpdateDestory.as_view(), name="project_view_retrieve_udpate_destroy"),
    path("persons/<int:pk>/", views.PersonRetrieveUpdateDestory.as_view(), name="person_view_retrieve_udpate_destroy"),
    path("datapoints/<int:pk>/", views.DataPointRetrieveUpdateDestory.as_view(), name="datapoint_view_retrieve_udpate_destroy"),
    path("objects/<int:pk>/", views.ProjectObjectRetrieveUpdateDestory.as_view(), name="object_view_retrieve_udpate_destroy"),
]
