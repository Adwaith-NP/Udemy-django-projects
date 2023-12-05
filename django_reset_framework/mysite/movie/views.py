from django.shortcuts import render
from rest_framework import viewsets
from .serializer import Movieserializer
from .models import Moviedata
# Create your views here.


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class= Movieserializer
    
class ActionViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ = 'Action')
    serializer_class = Movieserializer
    
class LoveViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ = 'Love')
    serializer_class = Movieserializer