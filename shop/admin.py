from django.contrib import admin
from django.utils.safestring import mark_safe

from shop.models import Category, Product, ProductImage, ProductProp
from shop.models import Order, OrderItem
from utils.utils import get_img_markup


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


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    # fields = ('image', 'image_prev',)


class ProductPropInline(admin.TabularInline):
    model = ProductProp
    extra = 1
    # fields = ('image', 'image_prev',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ProductPropInline]
    view_on_site = True
    list_display = ('__str__', 'category', 'old_price', 'discount', 'price', 'count', 'visible',
                    'image_prev')
    excludes = ('image',)
    list_filter = ('category', 'visible')
    fields = ('title', 'description', 'count', 'category', 'price', 'old_price', 'best_flag', 'image_prev_list',)
    readonly_fields = ('image_prev_list',)

    def discount_format(self, obj):
        if obj.discount > 0:
            return '-{} руб.'.format(obj.discount)
        return '-'

    discount_format.short_description = 'Скидка'

    def image_prev(self, obj):
        images = obj.get_images()
        if len(images) > 0:
            return get_img_markup(images[0])
        return ''

    image_prev.short_description = 'Фото'

    def image_prev_list(self, obj):
        img_list = []
        for image in obj.get_images():
            img_list.append(get_img_markup(image, size=128))
        return mark_safe(' '.join(img_list))

    image_prev_list.short_description = 'Картинки'


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    exclude = ['visible']
    extra = 0
    fields = ('product', 'count', 'props_list')
    readonly_fields = ('props_list',)

    def props_list(self, obj):
        res = []
        for prop in obj.props.all():
            res.append('%s: %s' % (prop.title, prop.value))
        return '\n'.join(res)

    props_list.short_description = 'Параметры'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ('__str__', 'products_count', 'status', 'total_price')
    list_filter = ('status',)
    readonly_fields = ('comment', 'first_name', 'phone', 'total_price')
    fields = ('comment', 'first_name', 'phone', 'status', 'total_price')

    def products_count(self, obj):
        return '%s' % (obj.items.count(),)

    products_count.short_description = 'Кол-во'
