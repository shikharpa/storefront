from django.urls import path, include
from bookapi.views import Booksviewset, reViewset
from rest_framework import routers


router= routers.DefaultRouter()
router.register(r'AllBooks', Booksviewset)
router.register(r'reviews', reViewset)


urlpatterns = [
    path('', include(router.urls))
]