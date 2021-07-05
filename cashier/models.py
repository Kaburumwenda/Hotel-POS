from django.db import models

from django.contrib.auth.models import User
from menu.models import Product
# Create your models here.

class ShopCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    table = models.CharField(max_length=50, default=1)
    date = models.DateField(auto_now_add=True, null=True)
    quantity = models.IntegerField()
    
    @property
    def price(self):
        return (self.product.Sprice)

    @property
    def amount(self):
        return (self.quantity * self.product.Sprice)
        
    @property
    def bcount(self):
        return (self.quantity * self.product.Bprice)        


class Order(models.Model):
    STATUS = (
        ('Paid', 'Paid'),
        ('Pending','Pending'),
        ('Cancelled', 'Cancelled'),
        )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    amount = models.IntegerField(default=0)
    table = models.CharField(max_length=50, default=1)
    status = models.CharField(max_length=50, choices=STATUS, default='Paid')
    create_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now=True, null=True)


    # def __str__(self):
    #     return self.product.title

    def title(self):
        return f"{self.product.title}"

    class Meta:  
        db_table = "order"  


class OrderProduct(models.Model):
    STATUS = (
        ('Paid', 'Paid'),
        ('Hide', 'Hide'),
        ('Cancelled', 'Cancelled'),
        )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(null=True)
    Sprice = models.DecimalField(max_digits=12, decimal_places=2, default='0.00')
    Bprice = models.DecimalField(max_digits=12, decimal_places=2, default='0.00')
    amount = models.DecimalField(max_digits=12, decimal_places=2, default='0.00')
    Bcount = models.DecimalField(max_digits=12, decimal_places=2, default='0.00')
    reference = models.CharField(max_length=20, null=True, default='SFR2021POS')
    table = models.CharField(max_length=50, default=1)
    status = models.CharField(max_length=20, choices=STATUS, null=True, default='Paid')
    create_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True, null=True)

    class Meta:  
        db_table = "orderproduct" 

    def __str__(self):
        return self.product.title

    def title(self):
        return f"{self.product.title}"
        
    def category(self):
        return f"{self.product.category}"    


class Table(models.Model):
    title = models.CharField(max_length=30)

    class Meta:  
        db_table = "table" 

    def __str__(self):
        return self.title
        