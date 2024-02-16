from django.db import models
from django.contrib.auth.models import User

# Create your models here.auth_user -auth-appname and user model name
#ceate a category table

class Category(models.Model):
    category_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True) #available or not ie true or false by default true ann false akknum pattum
    def __str__(self):
        return self.category_name
class Products(models.Model):
    product_name=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='image',null=True)#images okke extra oru folderil ann store chyyuka-upload_to-egottano upload chyyedath agott chyym
    description=models.CharField(max_length=100)
    def __str__(self):
        return self.product_name
class Carts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    options=(
        ('in-cart','in-cart'),#like key value pairs
        ('cancelled','cancelled'),
        ('order-placed','order-placed'),
    )
    status=models.CharField(max_length=100,choices=options,default='in-cart')# ivide kodukkuna choices mukalil kodutha options ayirikkum vruka ie incart,cancelled,order placed ithil default ayitt in-cart ann koduthittullath bakkiyoke nmmuk set chyyam ie cancelled and the order placed
class Orders(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cart=models.ForeignKey(Carts,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    address=models.TextField(max_length=255)
    email=models.EmailField()
    options=(
        ('order-placed','order-placed'),
        ('cancelled','cancelled'),
        ('dispatched','dispatched'),
        ('delivered','delivered')

    )
    status=models.CharField(max_length=100,choices=options,default='order-placed') # ithinte status change chyynm ordre placed koduthal incart mari order plced avnm