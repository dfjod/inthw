from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.ClientListCreate.as_view(), name = 'client-view-create'),
    path('projects/', views.ProjectListCreate.as_view(), name = 'project-view-create'),
    path('persons/', views.PersonListCreate.as_view(), name = 'person-view-create'),
    path('datapoints/', views.DataPointListCreate.as_view(), name = 'datapoint-view-create'),
    path('objects/', views.ProjectObjectListCreate.as_view(), name = 'object-view-create'),
    path('clients/<int:pk>/', views.ClientRetrieveUpdateDestroy.as_view(), name = 'client-view-retrieve-udpate-destroy'),
    path('projects/<int:pk>/', views.ProjectRetrieveUpdateDestory.as_view(), name = 'project-view-retrieve-udpate-destroy'),
    path('persons/<int:pk>/', views.PersonRetrieveUpdateDestory.as_view(), name = 'person-view-retrieve-udpate-destroy'),
    path('datapoints/<int:pk>/', views.DataPointRetrieveUpdateDestory.as_view(), name = 'datapoint-view-retrieve-udpate-destroy'),
    path('objects/<int:pk>/', views.ProjectObjectRetrieveUpdateDestory.as_view(), name = 'object-view-retrieve-udpate-destroy')
]