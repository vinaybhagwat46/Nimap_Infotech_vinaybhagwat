from django.shortcuts import render
from rest_framework import generics
from .serializer import ClientSerializer,ProjectSerializer
from .models import *

# Register a client
class addClient(generics.CreateAPIView):
    serializer_class=ClientSerializer

#List a clients
class listClient(generics.ListAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer

#Edit client info
class editClient(generics.RetrieveUpdateAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer

#Delete client Info
class deleteClient(generics.DestroyAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer

#Add new projects for a client and assign one or multiple users to those projects.
class createListProject(generics.ListCreateAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer

#Update or Delete project and its user or clients
class editDeleteProject(generics.RetrieveUpdateDestroyAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer

#Index Page
def index(request):
    return render(request,'index.html')
