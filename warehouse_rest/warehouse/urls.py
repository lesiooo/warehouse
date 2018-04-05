from django.conf.urls import url, include
from .views import *


api_urlpatterns = [
    url(r'^semi-finished-item/$', SemiFinishedItemList.as_view(), name='semi-finished-item-list'),
    url(r'^semi-finished-item/(?P<id>\d+)/$', SemiFinishedItemDetail.as_view(), name='semi-finished-item-rud'),

    url(r'finished-product/$', FinishedProductList.as_view(), name='finished-product-list'),
    url(r'finished-product/(?P<id>\d+)/$', FinishedProductDetail.as_view(), name='finished-product-rud'),
]

urlpatterns = [
    url(r'^api/', include(api_urlpatterns)),
    #url(r'^semi-finished-item', SemiFinishedItemListView.as_view(), name='semi-finished-item-list-view'),
    #url(r'^semi-finished-item/(?P<id>\d+)/$', SemiFisnishedItemDetailView.as_view(), name='semi-finished-item-detail-view'),

]

