from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True, null=True)
    updated_at = models.DateTimeField(_('Дата обновления'), auto_now=True, null=True)
    visible = models.BooleanField(_('Видимость'), default=True)

    class Meta:
        abstract = True


class OrderingBaseModel(BaseModel):
    visible = models.BooleanField(_('Видимость'), default=True)
    ordering = models.IntegerField(_('Порядок'), default=0, blank=True, null=True)

    class Meta:
        abstract = True
