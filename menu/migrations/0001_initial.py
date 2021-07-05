# Generated by Django 3.2.4 on 2021-07-01 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('Bprice', models.DecimalField(decimal_places=2, default='0.00', max_digits=12)),
                ('Sprice', models.DecimalField(decimal_places=2, default='0.00', max_digits=12)),
                ('offer', models.CharField(choices=[('True', 'True'), ('False', 'False')], default=False, max_length=30)),
                ('image', models.ImageField(upload_to='products/images')),
                ('category', models.CharField(choices=[('Wines', 'Wines'), ('Hard Drinks', 'Hard Drinks'), ('Beers', 'Beers'), ('Liqueurs & Creams', 'Liqueurs & Creams'), ('Soft Drinks', 'Soft Drinks'), ('Food & Drinks', 'Food & Drinks')], max_length=30)),
                ('subcategory', models.CharField(choices=[('Food', 'Food'), ('Whiskey', 'Whiskey'), ('Gin', 'Gin'), ('Brandy', 'Brandy'), ('Vodka', 'Vodka'), ('Rum', 'Rum'), ('Spirit', 'Spirit'), ('Liqueurs', 'Liqueurs'), ('Cream', 'Cream'), ('Soft Drink', 'Soft Drink'), ('Red Wine', 'Red Wine'), ('White Wine', 'White Wine'), ('Beer-Bottled', 'Beer-Bottled'), ('Beer-Can', 'Beer-Can')], max_length=30)),
                ('amount', models.IntegerField(default='1')),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('Bprice', models.DecimalField(decimal_places=2, default='0.00', max_digits=12)),
                ('Sprice', models.DecimalField(decimal_places=2, default='0.00', max_digits=12)),
                ('image', models.ImageField(upload_to='products/images')),
                ('category', models.CharField(choices=[('Wines', 'Wines'), ('Hard Drinks', 'Hard Drinks'), ('Beers', 'Beers'), ('Liqueurs & Creams', 'Liqueurs & Creams'), ('Soft Drinks', 'Soft Drinks'), ('Food & Drinks', 'Food & Drinks')], max_length=30)),
                ('subcategory', models.CharField(choices=[('Food', 'Food'), ('Whiskey', 'Whiskey'), ('Gin', 'Gin'), ('Brandy', 'Brandy'), ('Vodka', 'Vodka'), ('Rum', 'Rum'), ('Spirit', 'Spirit'), ('Liqueurs', 'Liqueurs'), ('Cream', 'Cream'), ('Soft Drink', 'Soft Drink'), ('Red Wine', 'Red Wine'), ('White Wine', 'White Wine'), ('Beer-Bottled', 'Beer-Bottled'), ('Beer-Can', 'Beer-Can')], max_length=30)),
                ('amount', models.IntegerField(default='1')),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'stock',
            },
        ),
    ]
