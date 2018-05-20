from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cart/', views.get_cart, name='shopping_cart'),
    path('add_to_cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>', views.remove_from_cart, name='remove_from_cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

