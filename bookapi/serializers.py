from rest_framework import serializers
from bookapi.models import Bookshelf, Reviews
#Create serialiizers here

class BooksSerializer(serializers.HyperlinkedModelSerializer):
    ISBN=serializers.ReadOnlyField()
    class Meta:
        model= Bookshelf
        fields=('ISBN', 'title', 'Author', 'genre', 'publish_year')
        
class reviewsSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Reviews
        fields="__all__"
