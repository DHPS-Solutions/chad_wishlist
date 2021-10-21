from django.urls import path

from accounts.views import AccountViewSet

# at the base of accounts/ show all accounts
urlpatterns = [
    path('', AccountViewSet.as_view({'get': 'list', 'post':'create'})),

]