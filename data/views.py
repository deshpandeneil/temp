from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.response import Response
from .serializers import DataSerializer
from .models import Data


class DataCreate(generics.CreateAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer


class DataList(generics.ListAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
