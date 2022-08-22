from rest_framework import serializers
from .models import Product

class productSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fileds = '__all__'