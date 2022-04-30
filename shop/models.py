from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    title = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return '/path/to/default/image'

        def __str__(self):
            return self.image

    class Meta:
        verbose_name_plural = 'Products'

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def transporting(self):
        transporting = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                transporting = True
        return transporting

    @property 
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product
    

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class DeliveryAddress(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    message = models.CharField(max_length=1000, null=True)
    number = models.IntegerField(default=0, null=True, blank=True) 
    email = models.CharField(max_length=200, null=True)
    dateAdded = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Delivery Address'

    def __str__(self):
        return self.address
    