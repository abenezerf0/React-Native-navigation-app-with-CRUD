from django.shortcuts import render
from rest_framework import generics
from .models import teacher
from .serializer import teachSerializer

class createEmp(generics.CreateAPIView):
    queryset = teacher.objects.all()
    serializer_class = teachSerializer
class listEmp(generics.ListAPIView):
    queryset = teacher.objects.all()
    serializer_class = teachSerializer
class deleteEmp(generics.DestroyAPIView):
    queryset = teacher.objects.all()
    serializer_class = teachSerializer
class updateEmp(generics.UpdateAPIView):
    queryset = teacher.objects.all()
    serializer_class = teachSerializer

# Create your views here.
