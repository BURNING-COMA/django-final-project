from django.urls import path
from .views import *

urlpatterns =[
    path('', projects, name='projects'),
    path('project/<str:pk>/', project, name='project'),
    path('create-project/', CreateProject, name='create-project'),
    path('update-project/<str:pk>', UpdateProject, name='update-project'),
    path('delete-project/<str:pk>', DeleteProject, name='delete-project'),
]