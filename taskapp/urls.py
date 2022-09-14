#created by user
from django.urls import path

from . import views

urlpatterns=[
    #path('',views.dashboard,name='taskapp-dashboard'),
    path('project/',views.project,name='taskapp-project'),
    path("logout", views.logout_request, name= "logout"),
    path('edit-project/<int:pk>/',views.edit_project,name="project-edit"),
    path('delete-project/<int:pk>/',views.delete_project,name="project-delete"),
    path('task/',views.index,name='taskapp-index'),#shows landing page,calls index function in views
    path('about/',views.about,name='taskapp-about'),
    path('delete/<int:pk>/',views.delete,name="taskapp-delete"),
    path('edit/<int:pk>/',views.edit,name="taskapp-edit"),
    path('report/',views.reports,name="taskapp-report"),
    path('file/',views.file,name="taskapp-file"),
    path('edit-file/<int:pk>/',views.edit_file,name="file-edit"),
    path('delete-file/<int:pk>/',views.delete_file,name="file-delete"),
    path('edit-report/<int:pk>/',views.edit_report,name="report-edit"),
    path('delete-report/<int:pk>/',views.delete_report,name="report-delete"),
    path('todo/',views.todo,name='taskapp-todo'),
    path('budget/',views.budget,name='taskapp-budget'),
    path('risk/',views.risk,name='taskapp-risk'),
    path('timeline/',views.timeline,name='taskapp-timeline'),


]