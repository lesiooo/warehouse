from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', OperationList.as_view(), name='operations-list'),
    url(r'^(?P<id>\d+)/$', OperationDetail.as_view(), name='operation-detail'),
    url(r'^cart/(?P<worker__username>\w+)/$', CartDetail.as_view(), name='cart-detail'),

    #url(r'^cart/', CartView.as_view(), name='cart'),

]