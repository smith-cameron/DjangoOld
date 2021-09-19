from django.shortcuts import render, redirect
from .models import *
from django.db.models import Sum

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    last_order = Order.objects.last()
    total_charge = last_order.total_price
    orderlist = Order.objects.aggregate(Sum('quantity_ordered'))['quantity_ordered__sum']
    ordertotal = Order.objects.aggregate(Sum('total_price'))['total_price__sum']
    context = {
        'order':orderlist,
        'totalprice': round(ordertotal,2),
        'total_charge':total_charge
    }
    return render(request, "store/checkout.html",context)

def purchase(request):
    if request.method == 'POST':
        selectedProduct = Product.objects.filter(id = request.POST['id'])
        quantity = int(request.POST["quantity"])
        price = quantity  * (float(selectedProduct[0].price))
        Order.objects.create(quantity_ordered=request.POST['quantity'], total_price=price)
        return redirect('/checkout')
