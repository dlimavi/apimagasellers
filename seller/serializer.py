from rest_framework import serializers
from .models import seller

class sellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = seller
        fields = ['idseller', 'descricao']










