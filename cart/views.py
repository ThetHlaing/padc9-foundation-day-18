from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Cart
# Create your views here.
def index(request):
    if request.method == 'POST':        
        post_data = request.POST
        print(Cart)
        new_cart = Cart(product_id=1,customer_id=1,qty=100,created_at = '2020-01-01')        
        new_cart.save()
        return HttpResponseRedirect('/cart')
    else:
        print("in the get request")
        return render(request,'cart_index.html')