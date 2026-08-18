from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['id', 'name', 'price', 'description']


        # some fields doesnot have to be changed by the user, so we can make them read-only fields. In this case, we are making the 'id' field read-only.   
        read_only_fields = ['id']
        