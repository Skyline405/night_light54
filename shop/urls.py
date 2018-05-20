from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.product_list, name='index'),
    path('product/<int:product_id>', views.product_details, name='product_details'),
    path('category/<int:category_id>', views.category_products, name='category_products'),
    path('order/create', views.create_order, name='create_order'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

