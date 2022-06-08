from django.urls import path
from stocks.views import StockView,CompanyView
from rest_framework import routers

from stocks.models import Stock
from rest_framework import routers

route = routers.DefaultRouter()
route.register(r"api",StockView,basename="sockview")
route.register(r"company",CompanyView,basename="companyview")

urlpatterns = route.urls