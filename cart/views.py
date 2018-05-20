from django.http import JsonResponse
from django.shortcuts import redirect, render

from cart.cart import Cart
from shop.models import Product
from cart.forms import CartForm


def add_to_cart(req, product_id, quantity=1):
    product = Product.objects.get(id=product_id)
    cart = Cart(req)
    cart.add(product, product.price, quantity)
    return JsonResponse({'success': True, 'count': cart.count()})


def remove_from_cart(req, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(req)
    cart.remove(product)
    return redirect('shopping_cart')


def get_cart(req):
    form = CartForm()
    return render(req, 'pages/cart_page.html', {'cart': Cart(req), 'form': form})
