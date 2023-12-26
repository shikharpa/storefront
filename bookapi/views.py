from django.shortcuts import render
from rest_framework import viewsets
from bookapi.models import Bookshelf, Reviews
from bookapi.serializers import BooksSerializer, reviewsSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters import rest_framework as filters

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

@method_decorator(cache_page(60*1), 'dispatch')
@method_decorator(vary_on_cookie, 'dispatch')
class Booksviewset(viewsets.ModelViewSet):
    queryset= Bookshelf.objects.all()
    serializer_class= BooksSerializer
    filter_backends = [filters.DjangoFilterBackend,]
    filterset_fields = ['Author', 'genre', 'publish_year']

    def get_queryset(self):
        return self.queryset.filter(is_deleted=False)
    
    def destroy(self, request, pk=None):
        bookshelf=self.get_object()
        bookshelf.is_deleted=True
        bookshelf.save()
        return Response({
            'message': "item has been deleted"
        })


    #Allbooks/ISBN/Allreviews
    @action(detail=True, methods=['get'])
    def Allreviews (self, request, pk=None):
        try:
            book= Bookshelf.objects.get(pk = pk)
            reviews= Reviews.objects.filter(book=book)
            review_serializer=reviewsSerializer(reviews, many=True, context={'request':request})
            return Response(review_serializer.data)
        except:
            return Response({
                'message': "error: book is not yet stored in database "
            })


class reViewset(viewsets.ModelViewSet):
    queryset=Reviews.objects.all()
    serializer_class=reviewsSerializer

