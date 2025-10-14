from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('suggestion_api/', views.suggestion_api, name='suggestion_api'),
]
