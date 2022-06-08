from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from stocks.views import StockView



urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('stocks.urls'))
]
