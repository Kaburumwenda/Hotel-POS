# Generated by Django 3.2.4 on 2021-07-02 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cashier', '0005_orderproduct_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
    ]
