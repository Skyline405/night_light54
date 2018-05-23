from django.shortcuts import render

from cart.cart import Cart
from shop.models import Category, Product, Order, OrderItem


def nl_render(req, template, context=None):
    if context is None:
        context = {}
    categories = Category.objects.filter(visible=True)
    cart = Cart(req)
    return render(req, template, {
        'categories': categories,
        'cart': cart,
        **context
    })


# Create your views here.
def index(req):
    return product_list(req)


def product_list(req):
    products = Product.objects.all()
    return nl_render(req, 'pages/products_page.html', {'products': products})


def product_details(req, product_id):
    product = Product.objects.get(pk=product_id)
    return nl_render(req, 'pages/product_details.html', {'product': product})


def category_products(req, category_id):
    products = Product.objects.filter(category=category_id)
    # products = Product.objects.all()
    return nl_render(req, 'pages/products_page.html', {'products': products})


def create_order(req):
    if req.method != 'POST':
        return nl_render(req, 'pages/access_denied.html')

    p = dict(req.POST)
    cart = Cart(req)
    order = Order()
    order.first_name = p['first_name'][0],
    order.phone = p['phone_number'][0],
    order.comment = p['comment'][0]
    order.save()

    for item in cart:
        order_item = OrderItem()
        order_item.order = order
        order_item.product = item.product
        order_item.count = item.quantity
        order_item.save()

    cart.check_out()
    return nl_render(req, 'pages/order_success.html')
