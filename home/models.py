from django.db import models
from authentications.models import User
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from pickle import TRUE
from .content_based import ContentBasedRecommender
# Create your models here.





class Product(models.Model):
    id=models.AutoField(primary_key=True,name="product_id")
    Name=models.CharField( max_length=50)
    description = models.TextField(max_length=1000)
    category=models.ForeignKey("Category", on_delete=models.CASCADE,null=True)
    price = models.DecimalField(max_digits=20, decimal_places=0,null=True)
    Production_country = models.CharField( max_length=50)
    image = models.ImageField( null= True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    
    
    
    def __str__(self):
        return self.Name

class Category(models.Model):
    id=models.AutoField(primary_key=True,name="category_id")
    Name = models.CharField(max_length=25)
    category_products = models.ManyToManyField("Product",related_name="categories")
    
    def __str__(self):
        return self.Name 


class Recommended(models.Model):
    id=models.AutoField(primary_key=True,name="recommend_id")
    product_name = models.ForeignKey("Product", on_delete=models.CASCADE) 
    recomended_devices = models.ManyToManyField("Product",related_name="aa") 
    
    def __str__(self):
        return str(self.product_name)


@receiver(post_save, sender=Product)
def recommend(sender, **kwargs):
    reco = Product.objects.all().values().last()
    x = ContentBasedRecommender()
    recommendation = x.get_recommendation(reco['product_id'])
    if recommendation != 0:
        reco_model = Recommended()

        reco_model.product_name_id = reco['product_id']
        reco_model.recommend_id = reco['product_id']

        reco_model.recomended_devices.set(recommendation)
        reco_model.save(force_insert=True)

       

class OrderItem(models.Model):
    id=models.AutoField(primary_key=True,name="orderitem_id")
    item = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 1)
    price = models.FloatField(default=0)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return str(self.user.email) + " " + str(self.item.Name)
    
class Order(models.Model):
    status_choices = (
        (1, 'PENDING'),
        (2, 'SUCCESS'),
        (3, 'FAILED'),
    )
    id=models.AutoField(primary_key=True,name="order_id")
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    # items=models.ManyToManyField("OrderItem", related_name="order")
    total_price = models.FloatField(default=0)
    profit = models.DecimalField(max_digits=50, decimal_places=2, default=0.00)
    status = models.IntegerField(choices = status_choices, default=1)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.user.email) + " " + str(self.total_price)

@receiver(pre_save, sender=OrderItem) 
def correct_price(sender, **kwargs):
    cart_items = kwargs['instance']
    price_of_product = Product.objects.get(product_id=cart_items.item.product_id)
    cart_items.price = cart_items.quantity * float(price_of_product.price)
    total_cart_items = OrderItem.objects.filter(user = cart_items.user )
    # cart = Order.objects.get(order_id = cart_items.cart.order_id)
    cart=Order.objects.create(user_id=cart_items.user.id)
    cart.total_price = cart_items.price
    multiplier = 10 / 100
    cart.profit = (cart.total_price * multiplier)
    cart.save()