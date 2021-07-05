from django.db import models

# Create your models here.
class Product(models.Model):
    CATEGORY = (  
        ('Wines', 'Wines'),
        ('Hard Drinks', 'Hard Drinks'),
        ('Beers', 'Beers'),
        ('Liqueurs & Creams', 'Liqueurs & Creams'),
        ('Soft Drinks', 'Soft Drinks'),
        ('Food & Drinks', 'Food & Drinks'),
    )
    SUBCATEGORY = (
        ('Food', 'Food'),
        ('Whiskey', 'Whiskey'),
        ('Gin', 'Gin'),
        ('Brandy', 'Brandy'),
        ('Vodka', 'Vodka'),
        ('Rum', 'Rum'),
        ('Spirit', 'Spirit'),
        ('Liqueurs', 'Liqueurs'),
        ('Cream', 'Cream'),
        ('Soft Drink', 'Soft Drink'),
        ('Red Wine', 'Red Wine'),
        ('White Wine', 'White Wine'),
        ('Beer-Bottled', 'Beer-Bottled'),
        ('Beer-Can', 'Beer-Can'),
    )
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
        )
    title = models.CharField(max_length=150)
    Bprice = models.DecimalField(max_digits=12, decimal_places=2, default='0.00')
    Sprice = models.DecimalField(max_digits=12, decimal_places=2, default='0.00')
    offer = models.CharField(max_length=30, choices=STATUS, default=False)
    image = models.ImageField(upload_to='products/images')
    category = models.CharField(max_length=30, choices=CATEGORY)
    subcategory = models.CharField(max_length=30, choices=SUBCATEGORY)
    amount = models.IntegerField(default='1')
    date = models.DateField(auto_now_add=True, blank = True)

    def __str__(self):
        return f"{self.title}"

    class Meta:  
        db_table = "product"  


class Stock(models.Model):
    CATEGORY = (
        ('Wines', 'Wines'),
        ('Hard Drinks', 'Hard Drinks'),
        ('Beers', 'Beers'),
        ('Liqueurs & Creams', 'Liqueurs & Creams'),
        ('Soft Drinks', 'Soft Drinks'),
        ('Food & Drinks', 'Food & Drinks'),
    )
    SUBCATEGORY = (
        ('Food', 'Food'),
        ('Whiskey', 'Whiskey'),
        ('Gin', 'Gin'),
        ('Brandy', 'Brandy'),
        ('Vodka', 'Vodka'),
        ('Rum', 'Rum'),
        ('Spirit', 'Spirit'),
        ('Liqueurs', 'Liqueurs'),
        ('Cream', 'Cream'),
        ('Soft Drink', 'Soft Drink'),
        ('Red Wine', 'Red Wine'),
        ('White Wine', 'White Wine'),
        ('Beer-Bottled', 'Beer-Bottled'),
        ('Beer-Can', 'Beer-Can'),
    )
    title = models.CharField(max_length=150)
    Bprice = models.DecimalField(max_digits=12, decimal_places=2, default='0.00')
    Sprice = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/images')
    category = models.CharField(max_length=30, choices=CATEGORY)
    subcategory = models.CharField(max_length=30, choices=SUBCATEGORY)
    amount = models.IntegerField(default='1')
    date = models.DateField(auto_now_add=True, blank = True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = "stock"
