from rest_framework import serializers
from .models import Category


#create serializers here
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    cat_id=serializers.ReadOnlyField()
    class Meta:
        model=Category
        fields="__all__"