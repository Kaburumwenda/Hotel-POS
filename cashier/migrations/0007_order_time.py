# Generated by Django 3.2.4 on 2021-07-03 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashier', '0006_remove_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='time',
            field=models.TimeField(auto_now=True, null=True),
        ),
    ]
