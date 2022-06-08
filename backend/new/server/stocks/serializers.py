from rest_framework import serializers
from stocks.models import Stock,Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class StockSerializer(serializers.ModelSerializer):
    stock_name = serializers.SlugRelatedField(queryset=Company.objects.all() ,slug_field='name')
    class Meta:
        model= Stock
        fields = ['id','stock_name','transaction_type','no_of_stocks','price_of_stock','transaction_date']
