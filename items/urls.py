from django.urls import path, include
from items.models import Item

from items.views import ItemViewSet


urlpatterns = [
    path('', ItemViewSet.as_view()),

]