from menu.models import Product
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from django.http import HttpResponse, HttpResponseRedirect
import json
from datetime import datetime, timedelta, time
from django.utils import timezone
from django.contrib.admin.views.decorators import staff_member_required
from .models import *
from .forms import ShopCartForm, TableChoicesForm, SearchForm


def cashier_pend_orders(request):
    current_user = request.user
    orders=Order.objects.filter(user_id=current_user.id).order_by('-id')
    context = {
               'orders': orders,
               }
    return render(request, 'cashier/pending.html', context)


@login_required(login_url='/login') # Check login
def cashier_pend_order_det(request,id):
    current_user = request.user
    order = Order.objects.get(user_id=current_user.id, id=id)
    orderitems = OrderProduct.objects.filter(order_id=id)
    orders=Order.objects.filter(user_id=current_user.id).order_by('-id')
    context = {
        'order': order,
        'orders':orders,
        'orderitems': orderitems,
    }
    return render(request, 'cashier/pending.html', context)


    
@staff_member_required(login_url='/guest/')    
def pending_orders_status(request, pk):
    published_item = get_object_or_404(Product, pk=pk)
    published_item.status = 'Active' if published_item.status == 'Cleared' else 'Cleared'
    published_item.save(update_fields=['status'])
    messages.success(request, 'Pending Order number {} {} successfully'.format(pk, published_item.status))
    return HttpResponseRedirect('/cashier/pending_orders/')    
