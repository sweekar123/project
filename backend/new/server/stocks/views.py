from django.shortcuts import render
from stocks.models import Stock,Company
from stocks.serializers import StockSerializer,CompanySerializer
from rest_framework import viewsets

# Create your views here.

class StockView(viewsets.ModelViewSet):
    queryset = Stock.objects.all().order_by("id")
    serializer_class = StockSerializer

class CompanyView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer