from django.db import models
from django.urls import reverse

from night_light.models import BaseModel
from shop.utils.utils import make_upload_path, get_img_markup


# Category
class Category(BaseModel):
    title = models.CharField('Название', default='', max_length=255)
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        default='',
        help_text='Краткое описание категории (Может быть пустым)'
    )
    image = models.ImageField(
        upload_to=make_upload_path,
        blank=True,
        default='',
        verbose_name='Картинка',
        help_text='Картинка, которая будет отображаться рядом с названием категории'
    )
    ordering = models.PositiveIntegerField('Порядок', default=0, help_text='Чем меньше значение, тем выше категория')

    @property
    def products_count(self):
        return self.products.count()

    @property
    def get_absolute_url(self):
        return reverse('category_products', args=[str(self.id)])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['ordering']
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


# Product
class Product(BaseModel):
    title = models.CharField('Название', default='', max_length=255)
    description = models.TextField('Описание', default='')
    count = models.PositiveIntegerField('Кол-во в наличии', default=0)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='products',
        verbose_name='Категория'
    )
    price = models.DecimalField(
        max_digits=8, decimal_places=2, default=0.00, verbose_name='Цена', help_text='Цена на товар в рублях'
    )
    discount = models.PositiveIntegerField('Скидка', default=0, help_text='Скидка на товар в процентах')
    # photo = models.ImageField(
    #     upload_to=make_upload_path,
    #     blank=True,
    #     default='',
    #     verbose_name='Фото товара'
    # )
    best_flag = models.BooleanField('"Best" флаг', default=False)

    def discount_price(self):
        return self.price - (self.price * self.discount / 100)

    discount_price.short_description = 'Цена со скидкой'

    def get_images(self):
        return self.images.filter(visible=True)

    @property
    def image(self):
        images = self.get_images()
        if len(images) > 0:
            return images[0]
        return None

    @property
    def get_absolute_url(self):
        return reverse('product_details', args=[str(self.id)])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']  # TODO: needs new first?
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class ProductImage(BaseModel):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Товар',
        help_text='Дополнительные картинки'
    )
    image = models.ImageField(
        upload_to=make_upload_path,
        verbose_name='Картинка'
    )
    ordering = models.PositiveIntegerField('Порядок', default=0, help_text='Порядок сортировки')

    @property
    def url(self):
        return self.image.url

    def image_prev(self):
        return get_img_markup(self.image)
    image_prev.short_description = 'Предпросмотр'

    class Meta:
        verbose_name = 'картинка'
        verbose_name_plural = 'картинки'
        managed = True


# Order
STATUS_WAITING = 'waiting'
STATUS_CONFIRMED = 'confirmed'
STATUS_SENDED = 'sended'
STATUS_DELIVERED = 'completed'

STATUS_CHOICES = (
    (STATUS_WAITING, 'Не принят'),
    (STATUS_CONFIRMED, 'Принят'),
    (STATUS_SENDED, 'Отправлен'),
    (STATUS_DELIVERED, 'Доставлен'),
)


class Order(BaseModel):
    comment = models.TextField('Комментарий', blank=True)
    first_name = models.CharField('Имя', default='', max_length=255)
    phone = models.CharField('Телефон', default='', max_length=255)
    status = models.CharField(
        'Статус',
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_WAITING,
    )

    def total_price(self):
        return sum(map(lambda item: item.product.discount_price, self.items.all()))

    total_price.short_description = 'Общая сумма'

    def __str__(self):
        return 'Заказ #%s' % (self.id,)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заказ", related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    count = models.PositiveIntegerField("Кол-во", default=1)

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'позиция'
        verbose_name_plural = 'позиции'
