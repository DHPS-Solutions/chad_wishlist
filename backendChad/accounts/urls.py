from django.urls import path

from accounts.views import AccountViewSet


urlpatterns = [
    path('', AccountViewSet.as_view({'get': 'list', 'post':'create'})),

]