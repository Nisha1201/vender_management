from django.urls import path
from .views import *

urlpatterns = [
    path('api/vendors/', vendor_list, name='vendor-list'),
    path('api/vendors/<int:vendor_id>/', vendor_detail, name='vendor-detail'),
    path('api/purchase_orders/', purchase_order_list, name='purchase-order-list'),
    path('api/purchase_orders/<int:po_id>/', purchase_order_detail, name='purchase-order-detail'),
    path('api/vendors/<int:vendor_id>/performance/', vendor_performance, name='vendor-performance'),
]


