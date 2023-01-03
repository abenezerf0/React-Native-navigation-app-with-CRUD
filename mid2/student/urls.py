from django.urls import path
from .views import *

urlpatterns = [
  
    path('create', createEmp.as_view()),
    path('list', listEmp.as_view()),
    path('delete/<int:pk>', deleteEmp.as_view()),
     path('update/<int:pk>', updateEmp.as_view()),




]