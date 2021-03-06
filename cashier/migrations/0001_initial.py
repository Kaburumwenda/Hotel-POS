# Generated by Django 3.2.4 on 2021-07-02 00:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table', models.CharField(default=1, max_length=50)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(null=True)),
                ('Sprice', models.DecimalField(decimal_places=2, default='0.00', max_digits=12)),
                ('Bprice', models.DecimalField(decimal_places=2, default='0.00', max_digits=12)),
                ('amount', models.DecimalField(decimal_places=2, default='0.00', max_digits=12)),
                ('Bcount', models.DecimalField(decimal_places=2, default='0.00', max_digits=12)),
                ('name', models.CharField(blank=True, default='SFR2021POS', max_length=20, null=True)),
                ('table', models.CharField(default=1, max_length=50)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Cleared', 'Cleared')], default='Active', max_length=20, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'pending',
            },
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(null=True)),
                ('Sprice', models.DecimalField(decimal_places=2, default='0.00', max_digits=12)),
                ('Bprice', models.DecimalField(decimal_places=2, default='0.00', max_digits=12)),
                ('amount', models.DecimalField(decimal_places=2, default='0.00', max_digits=12)),
                ('Bcount', models.DecimalField(decimal_places=2, default='0.00', max_digits=12)),
                ('reference', models.CharField(default='SFR2021POS', max_length=20, null=True)),
                ('status', models.CharField(choices=[('Paid', 'Paid'), ('Hide', 'Hide'), ('Cancelled', 'Cancelled')], default='Paid', max_length=20, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'orderproduct',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(null=True)),
                ('Sprice', models.DecimalField(decimal_places=2, default='0.00', max_digits=12)),
                ('Bprice', models.DecimalField(decimal_places=2, default='0.00', max_digits=12)),
                ('amount', models.DecimalField(decimal_places=2, default='0.00', max_digits=12)),
                ('table', models.CharField(default=1, max_length=50)),
                ('reference', models.CharField(max_length=20, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'order',
            },
        ),
    ]
