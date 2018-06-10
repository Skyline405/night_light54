import json

from django.http import JsonResponse
from django.shortcuts import redirect, render

from cart.cart import Cart
from shop.models import Product, OrderItem, ProductProp
from cart.forms import CartForm


def add_to_cart(req, product_id, quantity=1):
    props = json.loads(req.GET['props'])

    if not props:
        props = []

    product = Product.objects.get(id=product_id)

    order_item = OrderItem()
    order_item.product = product
    order_item.save()

    for prop in props:
        pp = ProductProp.objects.get(title=prop['name'], product_id=product.id, value=prop['value'])
        order_item.props.add(pp)

    cart = Cart(req)
    cart.add(order_item, product.price, quantity)
    return JsonResponse({'success': True, 'count': cart.count()})


def remove_from_cart(req, product_id):
    order_item = OrderItem.objects.get(id=product_id)
    cart = Cart(req)
    cart.remove(order_item)
    return redirect('shopping_cart')


def get_cart(req):
    form = CartForm()
    return render(req, 'pages/cart_page.html', {'cart': Cart(req), 'form': form})
