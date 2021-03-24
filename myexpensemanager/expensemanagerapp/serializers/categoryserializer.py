from rest_framework import serializers
from ..models import Category
from ..threads import TestThread


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

