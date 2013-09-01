from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns(
    '',
    url(r'^balance$', 'coinbase.views.balance'),
    url(r'^orders$', 'coinbase.views.orders'),
    url(r'^sell$', 'coinbase.views.sell'),
    url(r'^cfbox$', CrowdfundingBoxStat.as_view(), name='box'),
    url(r'^orderlist$', CrowdfundingOrderList.as_view(), name='orders'),
)
