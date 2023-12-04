from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Vendor
from .serializers import *

@api_view(['GET', 'POST'])
def vendor_list(request):
    if request.method == 'GET':
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def vendor_detail(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)

    if request.method == 'GET':
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        vendor.delete()
        return JsonResponse({'message': 'Vendor deleted successfully'}, status=204)



@api_view(['GET', 'POST'])
def purchase_order_list(request):
    if request.method == 'GET':
        vendor_id = request.query_params.get('vendor', None)
        if vendor_id:
            purchase_orders = PurchaseOrder.objects.filter(vendor__id=vendor_id)
        else:
            purchase_orders = PurchaseOrder.objects.all()

        serializer = PurchaseOrderSerializer(purchase_orders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def purchase_order_detail(request, po_id):
    po = get_object_or_404(PurchaseOrder, pk=po_id)

    if request.method == 'GET':
        serializer = PurchaseOrderSerializer(po)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PurchaseOrderSerializer(po, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        po.delete()
        return JsonResponse({'message': 'Purchase Order deleted successfully'}, status=204)

@api_view(['GET'])
def vendor_performance(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)

    performance_data = {
        'on_time_delivery_rate': vendor.on_time_delivery_rate,
        'quality_rating_avg': vendor.quality_rating_avg,
        'average_response_time': vendor.average_response_time,
        'fulfillment_rate': vendor.fulfillment_rate,
    }

    return Response(performance_data)
