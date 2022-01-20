from django.urls import path
from django.urls import path
from .views import *

urlpatterns = [
    path('', Calls.as_view(), name='calls'),
    path('calls_answered/', CallsAnswered.as_view(), name='calls_answered'),
    path('calls_missed/', CallsMissed.as_view(), name='calls_missed'),
    path('call-create', CallCreate.as_view(), name='call-create'),
    path('call-edit/<int:pk>/', CallEdit.as_view(), name='call-edit'),
    path('call-delete/<int:pk>/', CallDelete.as_view(), name='call-delete'),
    path('customers/', Customers.as_view(), name='customers'),
    path('customer/<int:pk>/', Customer.as_view(), name='customer'),
    path('tasks/', Tasks.as_view(), name='tasks'),
    path('tasks_completed/', TasksCompleted.as_view(), name='tasks_completed'),
    path('tasks_incompleted/', TasksIncompleted.as_view(), name='tasks_incompleted'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-edit/<int:pk>/', TaskEdit.as_view(), name='task-edit'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
]
