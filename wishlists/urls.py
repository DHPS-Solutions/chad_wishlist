from django.urls import path, include

from wishlists.views import WishlistViewSet


urlpatterns = [
    path('', WishlistViewSet.as_view({'get': 'list'})),

]