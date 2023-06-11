from django.urls import path
from . import views
urlpatterns = [
    path('', views.list_task, name='list-task'),
    path('create-task/', views.create_task, name='create-task'),
    path('update-task/<str:pk>/', views.update_task, name='update-task'),
    path('delete-task/<str:pk>/', views.delete_task, name='delete-task'),
    path('signup/', views.signup, name='signup'),
    path('search/', views.search, name='search'),

]

