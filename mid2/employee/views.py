from django.shortcuts import render
from rest_framework import generics
from .models import employee
from .serializer import empSerializer

class createEmp(generics.CreateAPIView):
    queryset = employee.objects.all()
    serializer_class = empSerializer
class listEmp(generics.ListAPIView):
    queryset = employee.objects.all()
    serializer_class = empSerializer
class deleteEmp(generics.DestroyAPIView):
    queryset = employee.objects.all()
    serializer_class = empSerializer
class updateEmp(generics.UpdateAPIView):
    queryset = employee.objects.all()
    serializer_class = empSerializer

# Create your views here.
