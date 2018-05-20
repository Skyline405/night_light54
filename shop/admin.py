from django.contrib import admin

from shop.models import Category, Product
from shop.models import Order, OrderItem
from shop.utils.utils import get_img_markup


# Models admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title_with_count', 'ordering', 'visible', 'image_prev')
    excludes = ('image',)
    list_filter = ('visible',)

    def title_with_count(self, obj):
        return '%s (%s)' % (obj.title, obj.products_count)

    title_with_count.short_description = 'Название'

    def image_prev(self, obj):
        return get_img_markup(obj.image)

    image_prev.short_description = 'Картинка'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    view_on_site = True
    list_display = ('__str__', 'category', 'price', 'discount_format', 'discount_price', 'count', 'visible', 'image')
    excludes = ('image',)
    list_filter = ('category', 'visible')

    def discount_format(self, obj):
        if obj.discount > 0:
            return '-{}%'.format(obj.discount)
        return '-'

    discount_format.short_description = 'Скидка'

    def image(self, obj):
        return get_img_markup(obj.photo)

    image.short_description = 'Фото'


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    exclude = ['visible']
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ('__str__', 'products_count', 'status', 'total_price')
    list_filter = ('status',)

    def products_count(self, obj):
        return obj.items.count()

    products_count.short_description = 'Кол-во товаров'
