from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from cart.cart import Cart
from shop.models import Category, Product, Order, OrderItem
from django.core.mail import send_mail


def nl_render(req, template, context=None):
    if context is None:
        context = {}
    categories = Category.objects.filter(visible=True)
    cart = Cart(req)
    return render(req, template, {
        'categories': categories,
        'cart': cart,
        'contact_email': settings.ADMIN_EMAIL,
        **context
    })


# Create your views here.
def index(req):
    return product_list(req)


def product_list(req):
    products = Product.objects.filter(visible=True, category__visible=True)

    paginator = Paginator(products, 9)

    page = req.GET.get('page')
    products = paginator.get_page(page)

    return nl_render(req, 'pages/products_page.html', {'products': products})


def product_details(req, product_id):
    product = Product.objects.get(pk=product_id, visible=True, category__visible=True)

    if not product:
        return nl_render(req, 'pages/404.html')

    category = Category.objects.get(pk=product.category.id)
    return nl_render(req, 'pages/product_details.html', {'product': product, 'current_category': category})


def category_products(req, category_id):
    category = Category.objects.get(pk=category_id, visible=True)

    if not category:
        return nl_render(req, 'pages/404.html')

    products = Product.objects.filter(category=category_id, visible=True, category__visible=True)

    paginator = Paginator(products, 9)

    page = req.GET.get('page')
    products = paginator.get_page(page)

    return nl_render(req, 'pages/products_page.html', {'products': products, 'current_category': category})


def create_order(req):
    if req.method != 'POST':
        return nl_render(req, 'pages/access_denied.html')

    p = dict(req.POST)
    cart = Cart(req)
    order = Order()
    order.first_name = p['first_name'][0]
    order.phone = p['phone_number'][0]
    order.city = p['city'][0]
    order.street = p['street'][0]
    order.building = p['building'][0]
    order.comment = p['comment'][0]

    last_order = Order.objects.all().order_by('-id')[0]
    if last_order:
        order.number = last_order.number + 1

    order.save()

    for item in cart:
        order.items.add(item.product)

    cart.check_out()

    subj = 'Получен заказ #%s на сумму %s' % (order.number, order.total_price(),)
    message = '''
        Поступил заказ #{number} на сумму {price}.
        ФИО: {name}
        Телефон: {phone}
        Адрес: {address}
        Комментарий: {comment}
    '''.format(
        number=order.number,
        price=order.total_price(),
        name=order.first_name[0],
        phone=order.phone[0],
        comment=order.comment,
        address=order.address()
    )

    send_mail(subj, message, settings.DEFAULT_FROM_EMAIL, [settings.ADMIN_EMAIL], fail_silently=True)

    return nl_render(req, 'pages/order_success.html')
