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


# Create your views here.
def index(request):
    data = Product.objects.all()
    current_user = request.user  # Access User Session information
    cart_count = ShopCart.objects.filter(user_id=current_user.id).count()
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total=0

    for rs in shopcart:
        total += rs.product.Sprice * rs.quantity

    form = TableChoicesForm 
    context = {
        'data': data,
        'shopcart':shopcart,
        'total':total,
        'cart_count':cart_count,
        'form':form,
    }
    return render(request, 'cashier/portal.html',context)


@staff_member_required(login_url='/guest/')
def addtoshopcart(request,id):
    url = request.META.get('HTTP_REFERER')  # get last url
    current_user = request.user  # Access User Session information
    checkinproduct = ShopCart.objects.filter(product_id=id) # Check product in shopcart


    if checkinproduct:
        control = 1 # The product is in the cart
    else:
        control = 0 # The product is not in the cart

    if request.method == 'POST':  # if there is a post
        form = ShopCartForm(request.POST)
        if form.is_valid():
           if control==1: # Update  shopcart
                data = ShopCart.objects.get(product_id=id)
                data.quantity += form.cleaned_data['quantity']
                ref = get_random_string(12).upper()
                data.reference = ref
                data.save()  # save data
           else : # Inser to Shopcart
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id =id
                data.quantity = form.cleaned_data['quantity']
                data.save()
        # messages.success(request, "Item added to Orders ")
        return HttpResponseRedirect(url)

    else: # if there is no post
        if control == 1:  # Update  shopcart
            data = ShopCart.objects.get(product_id=id)
            data.quantity += 1
            data.save()  #
        else:  #  Inser to Shopcart
            data = ShopCart()  # model ile bağlantı kur
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.save()  #
        # messages.success(request, "Item added to orders")
        return HttpResponseRedirect(url)


    
@staff_member_required(login_url='/guest/')    
def shopcart_plus(request, pk):
    url = request.META.get('HTTP_REFERER')  # get last url
    item = get_object_or_404(ShopCart, pk=pk)
    item.quantity +=1
    item.save(update_fields=['quantity'])
    return HttpResponseRedirect(url)

    
@staff_member_required(login_url='/guest/')    
def shopcart_minus(request, pk):
    url = request.META.get('HTTP_REFERER')  # get last url
    item = get_object_or_404(ShopCart, pk=pk)
    item.quantity -=1
    item.save(update_fields=['quantity'])
    return HttpResponseRedirect(url)
    

@staff_member_required(login_url='/guest/')
def deletefromcart(request,id):
    url = request.META.get('HTTP_REFERER')  # get last url
    ShopCart.objects.filter(id=id).delete()
    return HttpResponseRedirect(url)
    

@staff_member_required(login_url='/guest/')
def clearcart(request):
    url = request.META.get('HTTP_REFERER')  # get last url
    current_user = request.user
    ShopCart.objects.filter(user_id=current_user.id).delete() # Clear & Delete shopcart
    request.session['cart_items']=0
    return HttpResponseRedirect(url)


@staff_member_required(login_url='/guest/')
def order(request):
    current_user = request.user
    url = request.META.get('HTTP_REFERER')  # get last url
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total=0

    for rs in shopcart:
        total += rs.product.Sprice * rs.quantity

    if request.method == 'POST':
        form = TableChoicesForm(request.POST)
        if form.is_valid:
            for rs in shopcart:
                data=Order()
                data.user_id = current_user.id
                data.amount = total
                data.table = request.POST.get('table')
                data.status = request.POST.get('status')
                data.save()

                for rs in shopcart:
                    detail = OrderProduct()
                    detail.order_id = data.id # Order Id
                    detail.product_id = rs.product_id
                    detail.user_id = current_user.id
                    detail.quantity = rs.quantity
                    detail.Sprice = rs.product.Sprice
                    detail.Bprice = rs.product.Bprice
                    detail.Bcount = rs.bcount
                    detail.amount= rs.amount
                    detail.table = request.POST.get('table')
                    detail.save()
                    # ***Reduce quantity of sold product from Amount of Product
                    product = Product.objects.get(id=rs.product_id)
                    product.amount -= rs.quantity
                    product.save()
                    #************ <> *****************

                ShopCart.objects.filter(user_id=current_user.id).delete() # Clear & Delete shopcart
                request.session['cart_items']=0
                messages.success(request, "Your Order has been completed. Thank you ")
                return HttpResponseRedirect('/cashier')
            else:
                messages.warning(request, 'Something went wrong')
                return HttpResponseRedirect('/cashier')

    data = Product.objects.all()    
    context ={
        'shopcart':shopcart,
        'data': data,
    }

    return render(request, 'cashier/portal.html',context)



@staff_member_required(login_url='/guest/')
def menu_search(request):
    current_user = request.user
    url = request.META.get('HTTP_REFERER')  # get last url
    if request.method == 'POST': # check post
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query'] # get form input data
            data = Product.objects.filter(title__icontains=query)
            shopcart = ShopCart.objects.filter(user_id=current_user.id)

            total = 0

            for rs in shopcart:
                total += rs.product.Sprice * rs.quantity

            context = {
                'data': data,
                'query': query,
                'shopcart': shopcart,
                'total': total,
                       }
            return render(request, 'cashier/portal.html', context)

    return HttpResponseRedirect('/cashier/')



def search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        products = Product.objects.filter(title__icontains=q)

        results = []
        for rs in products:
            product_json = {}
            product_json = rs.title #+" > " + rs.category.title
            results.append(product_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)



