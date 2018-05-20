from django.contrib import admin

from extra_pages.models import DeliveryVariant, QuestionAnswer


@admin.register(DeliveryVariant)
class DeliveryVariantAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'region', 'duration', 'cost', 'visible')


@admin.register(QuestionAnswer)
class QuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'visible')
