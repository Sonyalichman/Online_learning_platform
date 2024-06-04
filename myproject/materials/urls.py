from django.urls import path
from . import views

urlpatterns = [
    path('', views.materials_list, name='materials_list'),
    path('upload/', views.upload_material, name='upload_material'),
    path('projects/', views.projects_list, name='projects_list'),
    path('projects/create/', views.create_project, name='create_project'),
    path('projects/<int:pk>/', views.project_details, name='project_details'),
    path('projects/<int:pk>/comment/', views.add_comment_to_project, name='add_comment_to_project'),
    path('materials/<int:pk>/comment/', views.add_comment_to_material, name='add_comment_to_material'),
]
