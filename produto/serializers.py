from rest_framework import serializers
from .models import titulo, preco, codproduto, idseller, qtndestoque

class tituloSerializer(serializers.ModelSerializer):
    class Meta:
        model = titulo
        fields = ['id', 'name', 'email']




