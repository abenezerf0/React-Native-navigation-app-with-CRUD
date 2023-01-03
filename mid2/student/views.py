from django.shortcuts import render
from rest_framework import generics
from .models import student
from .serializer import stuSerializer

class createEmp(generics.CreateAPIView):
    queryset = student.objects.all()
    serializer_class = stuSerializer
class listEmp(generics.ListAPIView):
    queryset = student.objects.all()
    serializer_class = stuSerializer
class deleteEmp(generics.DestroyAPIView):
    queryset = student.objects.all()
    serializer_class = stuSerializer
class updateEmp(generics.UpdateAPIView):
    queryset = student.objects.all()
    serializer_class = stuSerializer

# Create your views here.
