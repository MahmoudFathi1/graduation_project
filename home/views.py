from .models import Product ,Category,OrderItem , Order ,Recommended
from .serializers import HomeSerializers,CategorySerializers  ,RecommendedSerializers ,jsonOrder,jsonOrderItem
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, permissions
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
# from authentications.models import User



# @api_view(['Post','GET'])
# def Home_listAPI(request):
#     all_ads=Products.objects.all()
#     permission_classes = [permissions.IsAdminUser]
#     return Response(HomeSerializers(all_ads,many=True).data)


@api_view(['GET','Post'])
def Recommended_listAPI(request):
    all_ads=Recommended.objects.all()
    # permission_classes = [permissions.IsAdminUser]
    return Response(RecommendedSerializers(all_ads,many=True).data)

class product(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = HomeSerializers
    

@api_view(['GET','Post'])
def Category_listAPI(request):
    all_ads=Category.objects.all()
    # permission_classes = [permissions.IsAdminUser]
    return Response(CategorySerializers(all_ads,many=True).data)
    
class orderitem(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = jsonOrderItem


class order(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = jsonOrder
    
    
