
from os import name
from django.urls import path
from .import views
from .import pending

urlpatterns = [
    path('', views.index, name='cashier-portal'),
    path('addtoshopcart/<int:id>', views.addtoshopcart, name='addtoshopcart'),
    path('shopcart_plus/<int:pk>', views.shopcart_plus, name="shopcart_plus"),
    path('shopcart_minus/<int:pk>', views.shopcart_minus, name="shopcart_minus"),
    path('deletefromcart/<int:id>', views.deletefromcart, name='deletefromcart'),
    path('clearcart/', views.clearcart, name='clear-cart'),

    path('order/', views.order, name='cashier-order'),
    path('search/', views.menu_search, name="menu_search"),

    ############### PENDING
    path('pending/', pending.cashier_pend_orders, name='cashier_pend_orders'),
    path('pending/det/<int:id>/', pending.cashier_pend_order_det, name='cashier_pend_order_det')
]