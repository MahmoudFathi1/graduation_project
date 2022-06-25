from rest_framework import serializers
from .models import Product , Order , OrderItem ,Recommended,Category 

class HomeSerializers(serializers.ModelSerializer):
    category= serializers.CharField()
    class Meta:
        model = Product
        fields = ['product_id','Name','description','category','price','Production_country','image']

class CategorySerializers(serializers.ModelSerializer):
    category_products =  HomeSerializers(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['category_id','Name','category_products']
        
class RecommendedSerializers(serializers.ModelSerializer):
    product_name= HomeSerializers(read_only=True,)
    recomended_devices =  HomeSerializers(many=True, read_only=True,)
    class Meta:
        model = Recommended
        fields = ['product_name','recomended_devices']

        
class  jsonOrderItem(serializers.ModelSerializer):
    item= serializers.CharField(source='item.Name')
    price= serializers.CharField(source='item.price')
    image= serializers.CharField(source='item.image')
    class Meta:
        model = OrderItem
        fields = "__all__"
        
class  jsonOrder(serializers.ModelSerializer):
    # items= serializers.CharField(source=f"{OrderItem.quantity} of {OrderItem.item}")
    class Meta:
        model = Order
        fields = "__all__"      
        
