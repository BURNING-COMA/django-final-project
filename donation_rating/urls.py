from django.urls import path
from . import views

urlpatterns =[
    # path('', projects, name='projects'),
    # path('project/<str:pk>/', project, name='project'),
    # path('create-project/', CreateProject, name='create-project'),
    # path('update-project/<str:pk>', UpdateProject, name='update-project'),
    # path('delete-project/<str:pk>', DeleteProject, name='delete-project'),

    path('<str:project_id>', views.home, name='test_setup')
]