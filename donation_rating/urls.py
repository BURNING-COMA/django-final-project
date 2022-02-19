from django.urls import path
from . import views

urlpatterns =[
    # path('', projects, name='projects'),
    # path('project/<str:pk>/', project, name='project'),
    # path('create-project/', CreateProject, name='create-project'),
    # path('update-project/<str:pk>', UpdateProject, name='update-project'),
    # path('delete-project/<str:pk>', DeleteProject, name='delete-project'),

    path('project/<str:project_id>', views.home, name='proj_no'),
    path('update_rating/<int:project_id>', views.update_rating, name='update_rating'),
    path('donate/<int:project_id>', views.donate, name='donate'),

]
